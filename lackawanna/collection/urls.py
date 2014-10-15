from django.conf.urls import patterns, url
from collection import views

urlpatterns = patterns('',
        # Index (List of Projects)
        url(regex=r'^$',
            view=views.index,
            name='index'),

        # Collection Overview/Dashboard
        url(regex=r'^(?P<slug>\w+)/$',
            view=views.collection_page,
            name='page'),
)
