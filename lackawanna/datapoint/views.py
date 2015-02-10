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
from .models import Datapoint, Annotation
from .forms import FileForm, WebForm
from core.utils import get_keywords
import web_import
import file_import

# 3rd Party
from braces.views import LoginRequiredMixin
import textract

# Debug
import logging
logger = logging.getLogger(__name__)
import pdb

# REST API related
from rest_framework import generics, permissions, filters, viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datapoint.serializers import DatapointSerializer, AnnotationSerializer
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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class DatapointList(generics.ListAPIView):
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
    filter_fields = ('project', 'collections', 'owner')
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly, )


class DatapointViewSet(viewsets.ModelViewSet):
    queryset = Datapoint.objects.all()
    serializer_class = DatapointSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class DatapointListView(LoginRequiredMixin, ListView):
    model = Datapoint


class DatapointUploadView(LoginRequiredMixin, View):
    template_name = 'datapoint/datapoint_upload_choice.html'

    def get(self, request):
        return render(request, self.template_name)


class DatapointWebUploadView(LoginRequiredMixin, CreateView):
    template_name = 'datapoint/datapoint_web_upload_form.html'
    form_class = WebForm

    '''
    - Run newspaper over the link
    - Fill the fields out of form.instance (see file upload filefield for example) with this information
    - Redirect to the datapoint's page
    '''
    def form_valid(self, form):

        # TODO: Make this error catching
        '''Retrieve article's details using web_import.py's functions'''
        article = web_import.get_article(form.cleaned_data['url'])
        logger.debug("article details retrieved")

        '''Get the path to screenshot, open the file then attach the file to a Django file.'''
        screenshot = web_import.get_screenshot(form.cleaned_data['url'])
        screenshot_file = open(screenshot, 'r')
        django_screenshot = File(screenshot_file)
        logger.debug("screenshot retrieved")

        '''Attach information collected to the form.instance'''
        # Set uploader to request user
        form.instance.owner = self.request.user

        # Set filetype to web
        form.instance.filetype = "web"

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

        # for kw in article['keywords']:
        #     cur_datapoint.tags.add(kw)

        # Save Transcript
        if article['text']:
            transcript = Transcript(datapoint=cur_datapoint,
                                    owner=self.request.user,
                                    name='Auto-generated from site',
                                    text=article['text'])
            transcript.save()
            logger.debug("Transcript generated")

        return super(DatapointWebUploadView, self).form_valid(form)


"""
Upload a datapoint from a file to a chosen project.
If the form is found to be valid, processing is begun on the file.
"""


class DatapointFileUploadView(LoginRequiredMixin, CreateView):
    template_name = 'datapoint/datapoint_file_upload_form.html'
    model = Datapoint
    fields = ('project', 'name', 'file', 'description', 'author', 'source', 'url', 'publish_date')

    def form_valid(self, form):
        # Accessed repeatedly so making local variable to simplify code
        uploaded_file = self.get_form_kwargs().get('files')['file']

        if file_import.is_file_valid(uploaded_file):
            form.instance.filetype = file_import.get_filetype(uploaded_file)
            form.instance.file_extension = file_import.get_file_extension(uploaded_file)
        else:
            print "Uploaded file is not valid. Must stop the upload"
            # STOP THE UPLOAD SOMEHOW!

        # Set uploader to request user
        form.instance.owner = self.request.user

        # TODO: Make an exception here for files over a certain size/type
        # Extract text from file using Textract
        file_text = file_import.get_text(uploaded_file)

        # form.instance.tags = get_keywords(file_text)

        # Save datapoint's form. Do this here as it is required for transcription creation
        cur_datapoint = form.save()

        if file_text is not None:
            # Generate a transcript based on extracted text for the datapoint
            transcript = Transcript(datapoint=cur_datapoint,
                                    owner=self.request.user,
                                    name='Auto-generated from file',
                                    text=file_text)

        # TODO: Add an error message if something goes wrong and redirect to dashboard
        return super(DatapointFileUploadView, self).form_valid(form)


class DatapointUpdateView(LoginRequiredMixin, UpdateView):
    model = Datapoint
    fields = ('project', 'collections', 'name', 'author', 'source', 'url', 'publish_date', 'tags', 'annotations',
              'transcripts')
    success_url = reverse_lazy('datapoint:list')


class DatapointDeleteView(LoginRequiredMixin, DeleteView):
    model = Datapoint
    success_url = reverse_lazy('dashboard:index')
    success_message = "Datapoint was deleted successfully"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DatapointDeleteView, self).delete(request, *args, **kwargs)


class DatapointViewerView(LoginRequiredMixin, DetailView):
    template_name = 'datapoint/datapoint_detail.html'
    model = Datapoint

    def get_context_data(self, **kwargs):
        # Get current Datapoint object and add to (newly initialised) context
        context = super(DatapointViewerView, self).get_context_data(**kwargs)

        # List of all related transcripts
        context['transcripts'] = Transcript.objects.filter(datapoint=self.get_object())

        # Count of related transcripts
        context['transcript_count'] = context['transcripts'].count()

        # Return list of collections related to the project
        context['projects_collections'] = Collection.objects.filter(project=self.get_object().project.pk)

        # Return the collections that the datpoint is in.
        # context['datapoints_collections'] = self.get_object().collections
        # Return related project's details
        context['project'] = Project.objects.get(pk=self.get_object().project.pk)

        return context


class AnnotationListCreateView(generics.ListCreateAPIView):
    queryset = Annotation.objects.all()
    filter_fields = ('uri', 'owner', 'datapoint')
    serializer_class = AnnotationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class AnnotationSearchView(generics.ListCreateAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def list(self, request):
        uri = self.request.QUERY_PARAMS.get('uri', None)

        if uri is None:
            return Response({"Require URI to filter results"})
        else:
            queryset = Annotation.objects.filter(uri=uri)
            serializer = AnnotationSerializer(queryset, many=True)
            return Response({'rows': serializer.data, 'total': len(serializer.data)})


class AnnotationReadUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
