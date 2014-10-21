from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import View, FormView, UpdateView, ListView, DeleteView
from django.http import HttpResponse

from braces.views import LoginRequiredMixin

from .models import Datapoint
from .forms import FileForm


class DatapointListView(LoginRequiredMixin, ListView):
    model = Datapoint


class DatapointUploadView(LoginRequiredMixin, FormView):
    template_name = 'datapoint/datapoint_file_upload_form.html'
    form_class = FileForm

    def form_valid(self, form):
        datapoint = Datapoint(
            file=self.get_form_kwargs().get('files')['file'])
        datapoint.save()
        self.id = datapoint.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('datapoint', kwargs={'pk': self.id})


class DatapointUpdateView(LoginRequiredMixin, UpdateView):
    model = Datapoint
    fields = ('project', 'collections', 'name', 'author', 'source', 'url', 'publish_date', 'tags', 'annotations',
              'transcripts')
    success_url = reverse_lazy('datapoint:list')


class DatapointDeleteView(LoginRequiredMixin, DeleteView):
    model = Datapoint
    success_url = reverse_lazy('datapoint:list')


class DatapointViewerView(LoginRequiredMixin, View):
    def get(self):
        return HttpResponse("Individual dp page here!!")