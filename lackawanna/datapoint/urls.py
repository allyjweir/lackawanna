from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
        # Create Datapoint (Upload)
        url(regex=r'^upload/$',
            view=views.DatapointUploadView.as_view(),
            name='upload'),

        # Upload File
        url(regex=r'^upload/file/$',
            view=views.DatapointFileUploadView.as_view(),
            name='upload_file'),

        # Upload Large Files that require direct upload to S3.
        url(regex=r'^upload/large_file/$',
            view=views.DatapointLargeFileUploadView.as_view(),
            name='upload_large_file'),

        # Upload Webpage
        url(regex=r'^upload/web/$',
            view=views.DatapointWebUploadView.as_view(),
            name='upload_web'),

        # Update Datapoint
        url(regex=r'^(?P<pk>[\w.@+-]+)/update/$',
            view=views.DatapointUpdateView.as_view(),
            name='update'),


        # Delete Datapoint
        url(regex=r'^(?P<pk>[\w.@+-]+)/delete/$',
            view=views.DatapointDeleteView.as_view(),
            name='delete'),


        # Datapoint viewer
        url(regex=r'^(?P<pk>[\w.@+-]+)/$',
            view=views.DatapointViewerView.as_view(),
            name='viewer'),
)
