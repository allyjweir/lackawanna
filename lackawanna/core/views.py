import simplejson as json
from django.http import HttpResponse
from haystack.query import SearchQuerySet
import pdb
import jsonpickle




def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('query', ''))[:5]

    suggestions = [result.name for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    # Need to make specialised things for if it is different types, split the response json into different types
    class Result:
        def __init(self, name):
            self.name = name

    results = []
    for result in sqs:
        r = Result()
        r.name = result.name
        r.owner = result.owner
        r.description = result.description
        r.pk = result.pk
        results.append(r)

    results = jsonpickle.encode(results)
    return HttpResponse(results, content_type='application/json')
