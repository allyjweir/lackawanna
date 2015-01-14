from django.forms import widgets
from datapoint.models import Datapoint, Annotation
from rest_framework import serializers
from rest_framework.exceptions import ParseError


class TagListSerializer(serializers.Field):

    def to_internal_value(self, data):
        if type(data) is not list:
            raise ParseError("expected a list of data")
        return data

    def to_representation(self, obj):
        if type(obj) is not list:
            return [tag.name for tag in obj.all()]
        return obj


class DatapointSerializer(serializers.ModelSerializer):
    tags = TagListSerializer(required=False)

    class Meta:
        model = Datapoint
        fields = ('pk', 'owner', 'project', 'collections', 'name', 'description', 'author', 'source', 'url',
                                                        'publish_date', 'tags')


class AnnotationSerializer(serializers.ModelSerializer):
    tags = TagListSerializer(required=False)

    class Meta:
        model = Annotation
        fields = ('pk', 'owner', 'datapoint', 'annotator_schema_version', 'text', 'quote', 'uri', 'range_start',
				        				'range_end', 'range_startOffset', 'range_endOffset', 'tags')
