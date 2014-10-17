from django.conf.urls import patterns, url
from collection import views

urlpatterns = patterns('',
        # Index (List of Collections)
        url(regex=r'^$',
            view=views.CollectionListView.as_view,
            name='index'),

        # Collection Overview/Dashboard
        #url(regex=r'^(?P<slug>\w+)/$',
        #    view=views.collection_page,
        #    name='page'),

        # Create Collection
        url(regex=r'^create/$',
            view=views.CollectionCreateView.as_view(),
            name='create'),

        # Update Collection
        url(regex=r'^update/$',
            view=views.CollectionUpdateView.as_view(),
            name='update'),
)
