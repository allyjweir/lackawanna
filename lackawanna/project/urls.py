from django.conf.urls import patterns, url
from project import views

urlpatterns = patterns('',

        # Index
        url(regex=r'^$',
            view=views.index,
            name='project_index'),

)