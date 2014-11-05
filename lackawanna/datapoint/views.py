from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import View, FormView, UpdateView, ListView, DeleteView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone

import logging
logger = logging.getLogger(__name__)

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
        #Run newspaper over the link
        #Fill the fields out of form.instance (see file upload filefield for example) with this information
        #Redirect to the datapoint's page
        pass


"""
Upload a datapoint from a file to a chosen project.
If the form is found to be valid, processing is begun on the file.

Processing includes:
- Adding filetype to its field (used to identify what processing required)
- Term extraction (auto tagging)
- Thumbnail generation
- Initial transcript creation (put text of file into transcript)
- OCR of PDF files
"""
class DatapointFileUploadView(LoginRequiredMixin, CreateView):
    template_name = 'datapoint/datapoint_file_upload_form.html'
    model = Datapoint
    fields = ('uploaded_by', 'project', 'name', 'file', 'description', 'author', 'source', 'url', 'publish_date')
    success_url = reverse_lazy("datapoint:list")

    def form_valid(self, form):
        logger.info("The form is valid. Time to do stuff!")

        form.instance.file = self.get_form_kwargs().get('files')['file']
        
        return super(DatapointFileUploadView, self).form_valid(form)


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
