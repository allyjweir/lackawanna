from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404

from braces.views import LoginRequiredMixin

from .models import Project
from collection.models import Collection
from datapoint.models import Datapoint

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


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = 'project/project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        # Refer to the single object the view will display to filter based on it.
        context['collections'] = Collection.objects.filter(project = self.get_object())
        context['datapoints'] = Datapoint.objects.filter(project = self.get_object())
        # Return the context to load into the page.
        return context