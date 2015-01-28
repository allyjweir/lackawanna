import simplejson as json
from django.http import HttpResponse
from haystack.query import SearchQuerySet
import pdb

def autocomplete(request):
    #pdb.set_trace()
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('query', ''))[:5]
    suggestions = [result.name for result in sqs]
    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')
