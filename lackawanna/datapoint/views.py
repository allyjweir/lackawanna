from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import View, FormView, UpdateView, ListView, DeleteView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.contrib import messages
from django.core.files import File
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

# Lackawanna specific
from users.models import User
from project.models import Project
from collection.models import Collection
from transcript.models import Transcript
from .models import Datapoint
from .forms import FileForm, WebForm
import web_import

# 3rd Party
from braces.views import LoginRequiredMixin
import textract

# Debug
import logging
logger = logging.getLogger(__name__)
import pdb

# REST API related
from rest_framework import generics, permissions, filters
from datapoint.serializers import DatapointSerializer
from core.permissions import IsOwnerOrReadOnly


'''
API endpoint for accessing and updating datapoints

Limitations:
- Cannot get filename, file or filetype. This is for editing everything else.
- Does not currently support interaction with tags.
'''
class DatapointReadUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly,)


'''
API endpoint for getting list of datapoints

Limitations:
- No file creation
- No tags (YET!)
'''
class DatapointList(generics.ListAPIView):
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
    filter_fields = ('project', 'collections')

class DatapointListView(LoginRequiredMixin, ListView):
    model = Datapoint


class DatapointUploadView(LoginRequiredMixin, View):
    template_name = 'datapoint/datapoint_upload_choice.html'

    def get(self, request):
        return render(request, self.template_name)


class DatapointWebUploadView(LoginRequiredMixin, CreateView):
    template_name = 'datapoint/datapoint_web_upload_form.html'
    form_class = WebForm
    success_url = reverse_lazy('datapoint:list', args=[])
    success_message = "Datapoint was successfully created!"

    '''
    - Run newspaper over the link
    - Fill the fields out of form.instance (see file upload filefield for example) with this information
    - Redirect to the datapoint's page
    '''
    def form_valid(self, form):
        #pdb.set_trace()
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
        form.instance.owner = self.request.user

        # Save the URL as the one provided
        form.instance.url = form.cleaned_data['url']

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

        # Save screen shot, if exists
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
    fields = ('project', 'name', 'file', 'description', 'author', 'source', 'url', 'publish_date')
    success_url = reverse_lazy("datapoint:list")
    success_message = "Datapoint was successfully created!"


    def form_valid(self, form):
        logger.info("The form is valid. Time to do stuff!")

        # Set uploader to request user
        form.instance.owner = self.request.user
        #form.instance.file = self.get_form_kwargs().get('files')['file']
        #print self.get_form_kwargs().get('files')['file']

        ## Get the in memory file
        #file = self.get_form_kwargs().get('files')['file']  # Get the file from the upload
        #path = default_storage.save('temp/file.pdf', ContentFile(file.read()))

        #file_text = textract.process(path)

        cur_datapoint = form.save()

        #transcript = Transcript(datapoint=cur_datapoint,
        #                        creator=self.request.user,
        #                        name='Auto-generated from site',
        #                        text=file_text)

        messages.success(self.request, self.success_message)
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
        # Get current Datapoint object and add to (newly initialised) context
        context = super(DatapointViewerView, self).get_context_data(**kwargs)

        # List of all related transcripts
        context['transcripts'] = Transcript.objects.filter(datapoint = self.get_object())

        # Count of related transcripts
        context['transcript_count'] = context['transcripts'].count()

        #pdb.set_trace()

        # Return list of collections related to the project
        context['projects_collections'] = Collection.objects.filter(project = self.get_object().project.pk)

        # Return the collections that the datpoint is in.
        #context['datapoints_collections'] = self.get_object().collections
        # Return related project's details
        context['project'] = Project.objects.get(pk = self.get_object().project.pk)



        return context
