"""
All app specific API views called from the project root's urls.py URLConf thus:
    url(r"^api/", include ("lackawanna.api"), namespace="api"),
"""

from django.conf.urls import patterns, url

from datapoint import views as datapoint_views
from project import views as project_views
from collection import views as collection_views

urlpatterns = patterns("",

    # {% url "api:annotation-list" %}
    url(
        regex=r"^annotations/$",
        view=datapoint_views.AnnotationListCreateView.as_view(),
        name="annotation-list"
    ),

    # {% url "api:annotation-detail" annotation.pk %}
    url(
        regex=r"^annotations/(?P<pk>[-\w]+)/$",
        view=datapoint_views.AnnotationReadUpdateDeleteView.as_view(),
        name="annotation-detail"
    ),

    # {% url "api:datapoint-list" %}
    url(
        regex=r"^datapoints/$",
        view=datapoint_views.DatapointList.as_view(),
        name="datapoint-list"
    ),

    # {% url "api:datapoint-detail" datapoint.pk %}
    url(
        regex=r"^datapoints/(?P<pk>[-\w]+)/$",
        view=datapoint_views.DatapointReadUpdateDeleteView.as_view(),
        name="datapoint-detail"
    ),

    # {% url "api:project-list" %}
    url(
        regex=r"^projects/$",
        view=project_views.ProjectList.as_view(),
        name="project-list"
    ),

    # {% url "api:project-detail" project.pk %}
    url(
        regex=r"^projects/(?P<pk>[-\w]+)/$",
        view=project_views.ProjectReadUpdateDeleteView.as_view(),
        name="project-detail"
    ),

    # {% url "api:collection-list" %}
    url(
        regex=r"^collections/$",
        view=collection_views.CollectionList.as_view(),
        name="collection-list"
    ),

    # {% url "api:collection-detail" collection.pk %}
    url(
        regex=r"^collections/(?P<pk>[-\w]+)/$",
        view=collection_views.CollectionReadUpdateDeleteView.as_view(),
        name="collection-detail"
    ),
)
