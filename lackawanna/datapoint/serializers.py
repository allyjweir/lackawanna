from django.forms import widgets
from rest_framework import serializers
from datapoint.models import Datapoint, Annotation

class DatapointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Datapoint
		fields = ('pk', 'owner', 'project', 'collections', 'name', 'description', 'author', 'source', 'url', 'publish_date')

class AnnotationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Annotation
		fields = ('pk', 'owner', 'datapoint', 'annotator_schema_version', 'text', 'quote', 'uri', 'range_start', 'range_end', 'range_startOffset', 'range_endOffset')
