from django.shortcuts import render
from rest_framework import generics, permissions, filters, viewsets
from .serializers import TagSerializer
from core.permissions import IsOwnerOrReadOnly
from .models import Tag
from datapoint.models import Datapoint, Annotation
from braces.views import LoginRequiredMixin
from django.views.generic import DetailView


class TagReadUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    filter_fields = ('id', 'name', 'slug')


class TagDetailView(LoginRequiredMixin, DetailView):
    template_name = "tags/tag_detail.html"
    model = Tag

    def get_context_data(self, **kwargs):
        context = super(TagDetailView, self).get_context_data(**kwargs)
        context['related_datapoints'] = Datapoint.objects.filter(tags=self.get_object())
        context['related_annotations'] = Annotation.objects.filter(tags=self.get_object())

        return context
