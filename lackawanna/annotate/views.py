from django.shortcuts import render
from .models import Annotation
from rest_framework import generics, permissions
from annotate.serializers import AnnotationSerializer
from core.permissions import IsOwnerOrReadOnly


class AnnotationListCreateView(generics.ListCreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class AnnotationReadUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
        queryset = Annotation.objects.all()
        serializer_class = AnnotationSerializer
        permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
