from django.shortcuts import render
from .models import Annotation
from rest_framework import viewsets
from .serializers import AnnotationSerializer


class AnnotationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows annotations to be view or edited.
    """
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
