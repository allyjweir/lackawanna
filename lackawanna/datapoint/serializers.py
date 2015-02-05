from django.forms import widgets
from datapoint.models import Datapoint, Annotation
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from tags.serializers import TagSerializer
from tags.models import Tag


class DatapointSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Datapoint
        fields = ('pk', 'owner', 'project', 'collections', 'name', 'description', 'author', 'source', 'url',
                                                        'publish_date', 'tags')

    # def create(self, validated_data):
    #     tags = validated_data.pop("tags")
    #     tags = tags.split(' ')
    #     tags = validated_data.tags.split(' ')
    #     for tag in tags:
    #         Tag.objects.create(name=tag)
    #     datapoint = Datapoint.objects.create(**validated_data)
    #     return datapoint



class AnnotationSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Annotation
        fields = ('pk', 'owner', 'datapoint', 'annotator_schema_version', 'text', 'quote', 'uri', 'range_start',
				        				'range_end', 'range_startOffset', 'range_endOffset', 'tags')
