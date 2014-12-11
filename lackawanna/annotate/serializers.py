from django.forms import widgets
from rest_framework import serializers
from annotate.models import Annotation

class AnnotationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Annotation
		fields = ('pk', 'owner', 'datapoint', 'annotator_schema_version', 'text', 'quote', 'uri', 'range_start', 'range_end', 'range_startOffset', 'range_endOffset')
