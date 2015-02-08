from django.forms import widgets
from datapoint.models import Datapoint, Annotation
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from tags.serializers import TagSerializer
from tags.models import Tag
from users.serializers import UserSerializer
from users.models import User
from project.models import Project
import simplejson as json
import pdb


class Range():
    def __init__(self, start, end, startOffset, endOffset):
        self.start = start
        self.end = end
        self.startOffset = startOffset
        self.endOffset = endOffset


class RangeSerializer(serializers.BaseSerializer):
    start = serializers.CharField(max_length=50)
    end = serializers.CharField(max_length=50)
    startOffset = serializers.IntegerField()
    endOffset = serializers.IntegerField()

    def to_representation(self, obj):
        ranges = Range(obj[0], obj[1], obj[2], obj[3])
        return ranges.__dict__

    def to_internal_value(self, data):
        range_array = json.loads(data)

        start = range_array[0]['start']
        end = range_array[0]['end']
        startOffset = range_array[0]['startOffset']
        endOffset = range_array[0]['endOffset']

        return Range(start, end, startOffset, endOffset)


class DatapointSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = Datapoint
        fields = ('pk', 'owner', 'project', 'collections', 'name',
                  'description', 'author', 'source', 'url', 'publish_date',
                  'tags')

    def update(self, instance, validated_data):
        instance.project = validated_data.get('project', instance.project)
        instance.collections = validated_data.get('collections', instance.collections)
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.author = validated_data.get('author', instance.author)
        instance.source = validated_data.get('source', instance.source)
        instance.url = validated_data.get('url', instance.url)
        instance.publish_date = validated_data.get('publish_date', instance.publish_date)

        # Get all tags
        # If the tag doesn't have a slug (meaning it is an a new tag, and must be saved)
        # Create a new tag
        # Add it to the instance (How?)
        for tag in validated_data['tags']:
            if 'slug' not in tag:
                new_tag = Tag.objects.create(name=tag['name'])
                instance.tags.add(new_tag)

        instance.save()
        return instance


class AnnotationSerializer(serializers.Serializer):
    id = serializers.CharField(label="id")
    annotator_schema_version = serializers.CharField(max_length=8, allow_blank=True, required=False)
    text = serializers.CharField()
    quote = serializers.CharField()
    uri = serializers.CharField(max_length=100, min_length=None, allow_blank=True, required=False)
    ranges = RangeSerializer()
    owner = serializers.CharField(label='user')
    tags = TagSerializer(many=True, required=False)

    def update(self, instance, validated_data):
        instance.annotator_schema_version = validated_data.get('annotator_schema_version', instance.annotator_schema_version)
        instance.text = validated_data.get('text', instance.text)
        instance.quote = validated_data.get('quote', instance.quote)
        instance.uri = validated_data.get('uri', instance.uri)

        # Unpacking the ranges dict into 4 fields in instance.
        ranges = validated_data['ranges']
        instance.range_start = ranges.start
        instance.range_end = ranges.end
        instance.range_startOffset = ranges.startOffset
        instance.range_endOffset = ranges.endOffset

        instance.owner = User.objects.get(username=validated_data.get('owner'))
        instance.tags = validated_data.get('tags', instance.tags)

        instance.save()
        return instance

    def create(self, validated_data):
        validated_data.owner = User.objects.get(username = validated_data.get('owner'))
        return Annotation.objects.create(**validated_data)
