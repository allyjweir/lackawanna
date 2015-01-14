from django.contrib import admin
from datapoint.models import Datapoint, Tag, Annotation

admin.site.register(Datapoint)
admin.site.register(Tag)
admin.site.register(Annotation)
