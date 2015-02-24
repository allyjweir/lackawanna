from django.conf.urls import patterns, url, include
from .views import LackawannaSearchView

urlpatterns = patterns('',

                       url(r'^$', LackawannaSearchView.as_view(), name='lackawanna-search'),

                       )
