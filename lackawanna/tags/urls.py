from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',

        # Tag Overview
        url(regex=r'^(?P<slug>[\w.@+-]+)/$',
            view=views.TagDetailView.as_view(),
            name='detail'),


)
