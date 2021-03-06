from django.conf.urls import patterns, url
from dashboard import views

urlpatterns = patterns('',

        # Index
        url(regex=r'^$',
            view=views.DashboardView.as_view(),
            name='index'),

        url(regex=r'^autosearch/$',
            view=views.autocomplete,
            name='autocomplete-search'),

)
