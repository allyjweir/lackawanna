from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from braces.views import LoginRequiredMixin

from project.models import Project
from collection.models import Collection
from datapoint.models import Datapoint
from users.models import User

import simplejson as json
from haystack.query import SearchQuerySet

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)

        #Sidebar Recent lists
        context['latest_projects'] = Project.objects.all()[:3]
        context['latest_collections'] = Collection.objects.all()[:3]

        #grabstats
        context['users_count'] = User.objects.count()
        context['project_count'] = Project.objects.count()
        context['datapoint_count'] = Datapoint.objects.count()

        return context


'''Putting it here just now. May end up in core. As should the dashboard possibly. It doesn't really deserve its own app

http://django-haystack.readthedocs.org/en/latest/autocomplete.html
'''
def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(content_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.title for result in sqs]
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')
