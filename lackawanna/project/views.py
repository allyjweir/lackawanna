from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Projects index page here!")


def project_page(request):
    return HttpResponse("Individual project pages go here!")