from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from braces.views import LoginRequiredMixin

from .models import Project
from collection.models import Collection

class ProjectListView(LoginRequiredMixin, ListView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ('owner', 'name', 'description', 'website', 'status')
    success_url = reverse_lazy('project:list')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ('owner', 'name', 'description', 'website', 'status')
    success_url = reverse_lazy('project:list')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project:list')


def detail(request, slug):
    context = RequestContext(request)
    context_dict = {'slug':slug}
    try:
        project = Project.objects.get(slug=slug)
        context_dict['project'] = project

        collections = Collection.objects.filter(project=project)
        context_dict['collections'] = collections
    except Project.DoesNotExist:
        return HttpResponse("No project called this")

    return render_to_response('project/project_detail.html', context_dict, context)
