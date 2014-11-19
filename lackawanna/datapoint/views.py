from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import View, FormView, UpdateView, ListView, DeleteView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.core.files import File
import logging
logger = logging.getLogger(__name__)
from users.models import User
from project.models import Project
from transcript.models import Transcript
from braces.views import LoginRequiredMixin
from .models import Datapoint
from .forms import FileForm, WebForm
import web_import


class DatapointListView(LoginRequiredMixin, ListView):
    model = Datapoint


class DatapointUploadView(LoginRequiredMixin, View):
    template_name = 'datapoint/datapoint_upload_choice.html'

    def get(self, request):
        return render(request, self.template_name)


class DatapointWebUploadView(LoginRequiredMixin, CreateView):
    template_name = 'datapoint/datapoint_web_upload_form.html'
    form_class = WebForm
    success_url = reverse_lazy('datapoint:list')
    success_message = "Datapoint was successfully created!"

    '''
    - Run newspaper over the link
    - Fill the fields out of form.instance (see file upload filefield for example) with this information
    - Redirect to the datapoint's page
    '''
    def form_valid(self, form):
        logger.debug("Web Upload Form valid")

        '''Retrieve article's details using web_import.py's functions'''
        article = web_import.get_article(form.cleaned_data['url'])
        logger.debug("article details retrieved")

        '''Get the path to screenshot, open the file then attach the file to a django file.'''
        screenshot = web_import.get_screenshot(form.cleaned_data['url'])
        screenshot_file = open(screenshot, 'r')
        django_screenshot = File(screenshot_file)
        logger.debug("screenshot retrieved")


        '''Attach information collected to the form.instance'''
        # Set uploader to request user
        form.instance.uploaded_by = self.request.user

        # Save the title, if exists
        if article['title']:
            form.instance.name = article['title']
        else:
            form.instance.name = 'Extracted web page'

        # Save summary, if exists
        if article['summary']:
            form.instance.description = article['summary']

        # Save authors, if exists
        if article['authors']:
            form.instance.author = article['authors']

        # Save authors, if exists
        if article['publish_date']:
            form.instance.publish_date = article['publish_date']

        # Save screenshot, if exists
        if django_screenshot:
            form.instance.file = django_screenshot
            web_import.delete_file(screenshot)

        cur_datapoint = form.save()

        for kw in article['keywords']:
            cur_datapoint.tags.add(kw)

        # Save Transcript
        if article['text']:
            transcript = Transcript(datapoint=cur_datapoint,
                                    creator=self.request.user,
                                    name='Auto-generated from site',
                                    text=article['text'])
            transcript.save()
            logger.debug("Transcript generated")

        messages.success(self.request, self.success_message)
        return super(DatapointWebUploadView, self).form_valid(form)


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
    success_message = "Datapoint was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DatapointDeleteView, self).delete(request, *args, **kwargs)


class DatapointViewerView(LoginRequiredMixin, DetailView):
    template_name='datapoint/datapoint_detail.html'
    model = Datapoint

    def get_context_data(self, **kwargs):
        context = super(DatapointViewerView, self).get_context_data(**kwargs)
        context['transcripts'] = Transcript.objects.filter(datapoint = self.get_object())

        context['transcript_count'] = 0
        for transcript in context['transcripts']:
            context['transcript_count'] += 1

        return context
