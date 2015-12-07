# Django related
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

# 3rd Party
from braces.views import LoginRequiredMixin

# Lackawanna specific
from .models import Project
from .forms import ProjectCreationForm, ProjectUpdateForm
from collection.models import Collection
from datapoint.models import Datapoint

# REST API related
from rest_framework import generics, permissions, filters, viewsets, status
from project.serializers import ProjectSerializer
from core.permissions import IsOwnerOrReadOnly


'''This is the API endpoint for accessing individual projects.'''
class ProjectReadUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    filter_fields = ('id', 'owner')
    serializer_class = ProjectSerializer


'''
This is for accessing all Projects or creating a project
'''
class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    filter_fields = ('id', 'owner')
    serializer_class = ProjectSerializer


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    form_class = ProjectCreationForm
    template_name='project/project_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(ProjectCreateView, self).form_valid(form)


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    form_class = ProjectUpdateForm
    template_name='project/project_form.html'
    model = Project
    queryset = Project.objects.all()

    def get_success_url(self, **kwargs):
        return reverse_lazy('project:detail', kwargs={'slug':self.object.slug})


class ProjectDeleteView(SuccessMessageMixin, DeleteView):
    model = Project
    success_message = "Project was deleted successfully"
    success_url = reverse_lazy('project:list')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ProjectDeleteView, self).delete(request, *args, **kwargs)


class ProjectDetailView(LoginRequiredMixin, DetailView):
    template_name = 'project/project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ProjectDetailView, self).get_context_data(**kwargs)
        # Refer to the single object the view will display to filter based on it.
        context['collections'] = Collection.objects.filter(project = self.get_object())
        for c in context['collections']:
            c.datapoint_count = str(Datapoint.objects.filter(collections = c).count())
            logger.info(c.name + ":" + c.datapoint_count)
        context['datapoints'] = Datapoint.objects.filter(project = self.get_object())
        # Return the context to load into the page.
        return context
