from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from braces.views import LoginRequiredMixin

from project.models import Project
from collection.models import Collection

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        context['latest_projects'] = Project.objects.all()[:3]
        context['latest_collections'] = Collection.objects.all()[:3]
        return context