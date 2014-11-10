from django.conf.urls import patterns, url
from django.views.generic import TemplateView


from . import views

urlpatterns = patterns('',
        # Index (List of Collections)
        url(regex=r'^$',
            view=views.CollectionListView.as_view(),
            name='list'),


        # Create Collection
        url(regex=r'^create/$',
            view=views.CollectionCreateView.as_view(),
            name='create'),


        # Update Collection
        url(regex=r'^(?P<slug>[\w.@+-]+)/update/$',
            view=views.CollectionUpdateView.as_view(),
            name='update'),


        # Delete Collection
        url(regex=r'^(?P<slug>[\w.@+-]+)/delete/$',
            view=views.CollectionDeleteView.as_view(),
            name='delete'),


        # Collection Deletion Confirmation
        url(regex=r'^delete/confirmed/$',
            view=TemplateView.as_view(template_name='collection/collection_delete_done.html'),
            name='delete_confirmed'),


        # Collection Overview
        url(regex=r'^(?P<slug>[\w.@+-]+)/$',
            view=views.CollectionDetailView.as_view(),
            name='detail'),


        # Collection Settings Page
        url(regex=r'^(?P<slug>[\w.@+-]+)/$',
            view=views.CollectionSettingsView.as_view(),
            name='settings'),
)