"""
All app specific API views called from the project root's urls.py URLConf thus:
    url(r"^api/", include ("lackawanna.api"), namespace="api"),
"""

from django.conf.urls import patterns, url

from datapoint import views as datapoint_views
from project import views as project_views
from collection import views as collection_views
from tags import views as tags_views
from users import views as users_views

urlpatterns = patterns("",

    # {% url 'api:annotation-search' %}
    url(
        regex=r"^annotations/search/$",
        view=datapoint_views.AnnotationSearchView.as_view(),
        name="annotation-search"
    ),

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

    # {% url "api:tag-list" %}
    url(
        regex=r"^tags/$",
        view=tags_views.TagListCreateView.as_view(),
        name="tag-list"
    ),

    # {% url "api:tag-detail" tag.pk %}
    url(
        regex=r"^tags/(?P<pk>[-\w]+)/$",
        view=tags_views.TagReadUpdateView.as_view(),
        name="tag-detail"
    ),

    # {% url "api:savedsearch-list" %}
    url(
        regex=r"^savedsearch/$",
        view=datapoint_views.SavedSearchListCreateView.as_view(),
        name="savedsearch-list"
    ),

    # {% url "api:savedsearch-detail" savedsearch.search_term %}
    url(
        regex=r"^savedsearch/(?P<pk>[-\w]+)/$",
        view=datapoint_views.SavedSearchReadUpdateDeleteView.as_view(),
        name="savedsearch-detail"
    ),

        # {% url "api:users-list" %}
        url(
            regex=r"^users/$",
            view=users_views.UsersListView.as_view(),
            name="users-list"
        ),

    # {% url "api:users" user.username %}
    url(
        regex=r"^users/(?P<username>[-\w]+)/$",
        view=users_views.UserReadUpdateDeleteView.as_view(),
        name='users'
    )
)
