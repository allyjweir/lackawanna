from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',

        # List of user's Projects
        url(regex=r'^$',
            view=views.ProjectListView.as_view(),
            name='list'),

        # Project Details
        url(regex=r'^(?P<slug>\w+)/$',
            view=views.detail,
            name='page'),

        # Create Project
        url(regex=r'^create/$',
            view=views.ProjectCreateView.as_view(),
            name='create'),

        # Update Project
        url(regex=r'^update/$',
            view=views.ProjectUpdateView.as_view(),
            name='update'),

)
