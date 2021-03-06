# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView

from axes.decorators import watch_login
from allauth.account.views import login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',  # noqa
        TemplateView.as_view(template_name='pages/home.html'),
        name="home"),
    url(r'^about/$',
        TemplateView.as_view(template_name='pages/about.html'),
        name="about"),

    url(r'^admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    url(r'^service/', include(admin.site.urls)),

    # User management
    url(r'^users/', include("users.urls", namespace="users")),
    url(r'^accounts/login/$', watch_login(login)),  # For login rate limiting using django-axes
    url(r'^accounts/', include('allauth.urls')),

    # avatars
    url(r'^avatar/', include('avatar.urls')),

    # Markdown requirements
    url('^markdown/', include('django_markdown.urls')),

    # for DRF admin/testing view
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^dashboard/', include('dashboard.urls', namespace='dashboard')),

    url(r'^projects/', include('project.urls', namespace='project')),

    url(r'^collections/', include('collection.urls', namespace='collection')),

    url(r'^datapoints/', include('datapoint.urls', namespace='datapoint')),

    url(r'^apiv1/', include('core.apiv1', namespace='apiv1')),

    url(r'^transcripts/', include('transcript.urls', namespace='transcript')),

    url(r'^comments/', include('django_comments.urls')),

    url(r'^search/', include('search.urls', namespace='search')),

    url(r'^core/', include('core.urls',  namespace='core')),

    url(r'^tags/', include('tags.urls', namespace='tags')),

    url(r'^s3direct/', include('s3direct.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
