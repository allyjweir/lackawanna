from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView, View
from django.http import HttpResponse
from django.contrib import messages


from braces.views import LoginRequiredMixin

from .models import Collection
from datapoint.models import Datapoint

class CollectionListView(LoginRequiredMixin, ListView):
    model = Collection


class CollectionCreateView(LoginRequiredMixin, CreateView):
    model = Collection
    fields = ('owner', 'project', 'name', 'description',)
    success_url = reverse_lazy('collection:list')


class CollectionUpdateView(LoginRequiredMixin, UpdateView):
    model = Collection
    fields = ('owner', 'project', 'name', 'description',)
    success_url = reverse_lazy('collection:list')


class CollectionDeleteView(LoginRequiredMixin, DeleteView):
    model = Collection
    success_url = reverse_lazy('collection:delete_confirmed')
    success_message = "Project was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CollectionDeleteView, self).delete(request, *args, **kwargs)


class CollectionDetailView(LoginRequiredMixin, DetailView):
    template_name = 'collection/collection_detail.html'
    model = Collection

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        context['datapoints'] = Datapoint.objects.filter(collections =  self.get_object())
        return context


class CollectionSettingsView(LoginRequiredMixin, View):
    template_name = 'collection/collection_settings.html'
    model = Collection

    def get_context_data(self, **kwargs):
        context = super(CollectionSettingsView, self).get_context_data(**kwargs)
        return context
