from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.http import HttpResponse

from braces.views import LoginRequiredMixin

from .models import Collection

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
    success_url = reverse_lazy('collection:list')


class CollectionDetailView(LoginRequiredMixin, DetailView):
    template_name = 'collection/collection_detail.html'
    model = Collection

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context
