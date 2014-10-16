from django.conf.urls import patterns, url
from dashboard import views

urlpatterns = patterns('',

        # Index
        url(regex=r'^$',
            view=views.IndexView,
            name='index'),

)