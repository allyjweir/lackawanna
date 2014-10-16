from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.http import HttpResponse

from braces.views import LoginRequiredMixin

from .models import Project

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ('name', 'description', 'website', 'status')


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    fields = ('name', 'description', 'website', 'status')


def list(request):
    return HttpResponse("Projects index page here!")


def detail(request):
    return HttpResponse("Individual project pages go here!")

