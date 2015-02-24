from django.shortcuts import render, render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic import View, FormView, UpdateView, ListView, DeleteView, DetailView, CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
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
from .models import Datapoint, Annotation, SavedSearch
from .forms import DatapointFileUploadForm, DatapointWebRetrievalForm
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
from .serializers import DatapointSerializer, AnnotationSerializer, SavedSearchSerializer
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
    form_class = DatapointWebRetrievalForm
    template_name = 'datapoint/datapoint_web_upload_form.html'

    '''
    - Run newspaper over the link
    - Fill the fields out of form.instance (see file upload filefield for example) with this information
    - Redirect to the datapoint's page
    '''
    def form_valid(self, form):
        data = form.cleaned_data

        # TODO: Make this error catching
        '''Retrieve article's details using web_import.py's functions'''
        article = web_import.get_article(form.cleaned_data['url'])

        '''Get the path to screenshot, open the file then attach the file to a Django file.'''
        screenshot = web_import.get_screenshot(form.cleaned_data.get('url'))
        django_screenshot = File(open(screenshot, 'r'))
        logger.debug("screenshot retrieved")

        # Save screen shot, if exists
        if django_screenshot:
            form.instance.file = django_screenshot
            web_import.delete_file(screenshot)
        else:
            logger.error('No screenshot attached to web import datapoint object.')

        '''Attach information collected to the form.instance'''
        form.instance.owner = self.request.user
        form.instance.filetype = "web"
        form.instance.url = form.cleaned_data.get('url')
        form.instance.title = article.get('title', 'No title found')
        form.instance.summary = article.get('summary', '')
        # form.instance.publish_date = article.get('publish_date', '1970-01-01')
        authors = article.get('authors', 'No author provided')
        form.instance.author = ', '.join(authors)

        cur_datapoint = form.save()

        # Save Transcript
        # if article['text']:
            # transcript = Transcript(cur_datapoint.pk,
            #                         self.request.user,
            #                         'Automated transcript',
            #                         article['text'])
            # transcript.save()
            # logger.debug("Transcript generated")

        return super(DatapointWebUploadView, self).form_valid(form)


"""
Upload a datapoint from a file to a chosen project.
If the form is found to be valid, processing is begun on the file.
"""


class DatapointFileUploadView(LoginRequiredMixin, CreateView):
    template_name = 'datapoint/datapoint_file_upload_form.html'
    form_class = DatapointFileUploadForm

    def form_valid(self, form):
        data = form.cleaned_data
        pdb.set_trace()
        # Accessed repeatedly so making local variable to simplify code
        uploaded_file = data.get('file', None)

        # TODO: Correct file validation.
        # if file_import.is_file_valid(uploaded_file):
        form.instance.filetype = file_import.get_filetype(uploaded_file)
        form.instance.file_extension = file_import.get_file_extension(uploaded_file)
        # else:
            # logger.error("Invalid file type. Not uploaded to system.")
            # STOP THE UPLOAD SOMEHOW AND SHOW ERROR!

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
    success_message = "Datapoint was deleted successfully"

    def get_success_url(self):
        return reverse_lazy('project:detail', kwargs={'slug':self.object.project.slug})

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DatapointDeleteView, self).delete(request, *args, **kwargs)


class DatapointViewerView(LoginRequiredMixin, DetailView):
    template_name = 'datapoint/datapoint_detail.html'
    model = Datapoint

    def get_context_data(self, **kwargs):
        # Get current Datapoint object and add to (newly initialised) context
        context = super(DatapointViewerView, self).get_context_data(**kwargs)

        # All related transcripts
        context['transcripts'] = Transcript.objects.filter(datapoint=self.get_object())
        context['transcript_count'] = context['transcripts'].count()

        # All related annotations
        context['annotations'] = Annotation.objects.filter(datapoint=self.get_object())
        context['annotation_count'] = context['transcripts'].count()

        # Parent project
        context['project'] = Project.objects.get(pk=self.get_object().project.pk)
        # Collections related to parent project
        context['projects_collections'] = Collection.objects.filter(project=self.get_object().project.pk)

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


class SavedSearchReadUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedSearch.objects.all()
    filter_fields = ('search_term', 'owner')
    serializer_class = SavedSearchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)


class SavedSearchListCreateView(generics.ListCreateAPIView):
    queryset = SavedSearch.objects.all()
    serializer_class = SavedSearchSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)
