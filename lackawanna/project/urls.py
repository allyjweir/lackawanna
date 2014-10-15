from django.conf.urls import patterns, url
from project import views

urlpatterns = patterns('',

        # Index (List of Projects)
        url(regex=r'^$',
            view=views.index,
            name='index'),

        # Project Overview/Dashboard
        url(regex=r'^/(?P<slug>\w+)/$',
            view=views.project_page,
            name='page'),

)
