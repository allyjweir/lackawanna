from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.http import HttpResponse

from braces.views import LoginRequiredMixin

from .models import Collection

class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection


class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    fields = ('owner', 'project', 'name', 'description',)
    success_url = reverse_lazy('project:list')


class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Collection
    fields = ('owner', 'project', 'name', 'description',)
    success_url = reverse_lazy('collection:list')


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Collection
    success_url = reverse_lazy('collection:list')


def detail(request, slug):
    return HttpResponse("Individual collection pages go here!")