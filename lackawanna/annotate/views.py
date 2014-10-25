from django.shortcuts import render
from .models import Annotation
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class AnnotationCreateReadView(ListCreateAPIView):
    model = Annotation

class AnnotationReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    model = Annotation