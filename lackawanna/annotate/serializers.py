from .models import Annotation
from rest_framework import serializers


class AnnotationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Annotation
        fields = ('datapoint', 'owner', 'annotator_schema_version', 'text', 'quote', 'uri', 'range_start', 'range_end',
                    'range_startOffset', 'range_endOffset', )