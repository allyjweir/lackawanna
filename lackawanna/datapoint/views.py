from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import View, FormView, UpdateView, ListView, DeleteView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

from users.models import User
from project.models import Project

from braces.views import LoginRequiredMixin

from .models import Datapoint
from .forms import FileForm, WebForm


class DatapointListView(LoginRequiredMixin, ListView):
    model = Datapoint


class DatapointUploadView(LoginRequiredMixin, View):
    template_name = 'datapoint/datapoint_upload_choice.html'

    def get(self, request):
        return render(request, self.template_name)


class DatapointWebUploadView(LoginRequiredMixin, FormView):
    template_name = 'datapoint/datapoint_web_upload_form.html'
    form_class = WebForm

    def form_valid(self, form):
        #Do something here if the form is found valid!
        pass

    def get_success_url(self):
        return reverse('datapoint')


class DatapointFileUploadView(LoginRequiredMixin, FormView):
    template_name = 'datapoint/datapoint_file_upload_form.html'
    form_class = FileForm

    def form_valid(self, form):
        datapoint = Datapoint(
            file=self.get_form_kwargs().get('files')['file'],
            uploaded_by=User.objects.get(username=self.request.user.username),
            project=Project.objects.get(name="London Riots"))

        form.process()
        datapoint.save()
        self.id = datapoint.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("datapoint:viewer", kwargs={"pk": self.id})


class DatapointUpdateView(LoginRequiredMixin, UpdateView):
    model = Datapoint
    fields = ('project', 'collections', 'name', 'author', 'source', 'url', 'publish_date', 'tags', 'annotations',
              'transcripts')
    success_url = reverse_lazy('datapoint:list')


class DatapointDeleteView(LoginRequiredMixin, DeleteView):
    model = Datapoint
    success_url = reverse_lazy('datapoint:list')


class DatapointViewerView(LoginRequiredMixin, DetailView):
    template_name='datapoint/datapoint_detail.html'
    model = Datapoint

    def get_context_data(self, **kwargs):
        context = super(DatapointViewerView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
