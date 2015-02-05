from django.shortcuts import render

# REST API related
from rest_framework import generics, permissions, filters, viewsets
from .serializers import TagSerializer
from core.permissions import IsOwnerOrReadOnly
from .models import Tag


class TagReadUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
