from django.conf.urls import patterns, url, include
from . import views


urlpatterns = [
    url(
        regex = r"^api/$",
        view = views.AnnotationCreateReadView.as_view(),
        name = 'annotation_rest_api'
    ),

    url(
        regex = r"^api/(?P<pk>[-\w]+)/$",
        view = views.AnnotationReadUpdateDeleteView.as_view(),
        name = 'annotation_rest_api'
    ),


]