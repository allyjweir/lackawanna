from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
        # Index (List of Datapoints)
        url(regex=r'^auto/$',
            view=views.autocomplete,
            name='autocomplete'),

    )
