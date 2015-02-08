# Django imports
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views import generic as django_generic
from django.http import HttpResponse
from django.contrib import messages

# 3rd Party Package imports
from braces.views import LoginRequiredMixin

#Lackawanna Specific imports
from .models import Collection
from .forms import CollectionCreationForm
from datapoint.models import Datapoint

# REST API related imports
from rest_framework import generics as rest_generics, permissions, filters
from collection.serializers import CollectionSerializer
from core.permissions import IsOwnerOrReadOnly


class CollectionList(rest_generics.ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    filter_fields = ('project', 'owner')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


class CollectionReadUpdateDeleteView(rest_generics.RetrieveUpdateDestroyAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


class CollectionListView(LoginRequiredMixin, django_generic.ListView):
    model = Collection


class CollectionCreateView(LoginRequiredMixin, django_generic.CreateView):
    form_class = CollectionCreationForm
    template_name = 'collection/collection_create.html'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(CollectionCreateView, self).form_valid(form)


class CollectionUpdateView(LoginRequiredMixin, django_generic.UpdateView):
    model = Collection
    fields = ('owner', 'project', 'name', 'description',)
    success_url = reverse_lazy('collection:list')


class CollectionDeleteView(LoginRequiredMixin, django_generic.DeleteView):
    model = Collection
    success_url = reverse_lazy('collection:delete_confirmed')
    success_message = "Project was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(CollectionDeleteView, self).delete(request, *args, **kwargs)


class CollectionDetailView(LoginRequiredMixin, django_generic.DetailView):
    template_name = 'collection/collection_detail.html'
    model = Collection

    def get_context_data(self, **kwargs):
        context = super(CollectionDetailView, self).get_context_data(**kwargs)
        context['datapoints'] = Datapoint.objects.filter(collections =  self.get_object())
        return context


class CollectionSettingsView(LoginRequiredMixin, django_generic.View):
    template_name = 'collection/collection_settings.html'
    model = Collection

    def get_context_data(self, **kwargs):
        context = super(CollectionSettingsView, self).get_context_data(**kwargs)
        return context
