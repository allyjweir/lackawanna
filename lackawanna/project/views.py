from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.http import HttpResponse

from braces.views import LoginRequiredMixin

from .models import Project

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


def detail(request):
    return HttpResponse("Individual project pages go here!")

