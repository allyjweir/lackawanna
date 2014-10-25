"""
All app specific API views called from the project root's urls.py URLConf thus:
    url(r"^api/", include ("lackawanna.api"), namespace="api"),
"""

from django.conf.urls import patterns, url

from annotate import views as annotate_views

urlpatterns = patterns("",

    # {% url "api:annotate" %}
    url(
        regex=r"^annotate/$",
        view=annotate_views.AnnotationCreateReadView.as_view(),
        name="annotate"
    ),

    # {% url "api:annotate" annotation.pk %}
    url(
        regex=r"^annotate/(?P<pk>[-\w]+)/$",
        view=annotate_views.AnnotationReadUpdateDeleteView.as_view(),
        name="annotate"
    ),


)