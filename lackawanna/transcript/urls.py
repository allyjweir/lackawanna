from django.conf.urls import patterns, url
from . import views

"""
The DREAM of this urls.py is to extend the datapoint urls.py

Ultimately there is a one-to-many relationship between a datapoint and a transcript. This means a transcript will always
belong to a singular datapoint. Therefore its url should be within a datapoint's url.

I propose a url structure as such:

    lackawanna.io/datapoint/15/transcripts/create for CreateView
    lackawanna.io/datapoint/15/transcripts/2 for viewer of specific transcript

And so on.

Hopefully this is clear!


HOWEVER, for now it is in the root urls.py because it is difficult to figure out how to do this reliably!
"""
urlpatterns = patterns('',
        # List Transcripts
        #(regex=r'^/$',
        #    view=views.TranscriptListView.as_view(),
        #    name='list'),


        # Create Transcript
        url(regex=r'^upload/$',
            view=views.TranscriptCreateView.as_view(),
            name='upload'),


        # Update Transcript
        url(regex=r'^(?P<pk>[\w.@+-]+)/update/$',
            view=views.TranscriptUpdateView.as_view(),
            name='update'),


        # Delete Transcript
        url(regex=r'^(?P<pk>[\w.@+-]+)/delete/$',
            view=views.TranscriptDeleteView.as_view(),
            name='delete'),


        # Transcript viewer
        url(regex=r'^(?P<pk>[\w.@+-]+)/$',
            view=views.TranscriptViewerView.as_view(),
            name='viewer'),
)
