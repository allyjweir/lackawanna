from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Collection index page here!")


def collection_page(request):
    return HttpResponse("Individual collection pages go here!")