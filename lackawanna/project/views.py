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
    success_url = reverse_lazy('project:project_list')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    success_url = reverse_lazy('project:project_list')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    success_url = reverse_lazy('project:project_list')


def detail(request):
    return HttpResponse("Individual project pages go here!")

