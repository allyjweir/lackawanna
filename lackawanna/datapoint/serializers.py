from django.forms import widgets
from .models import Datapoint, Annotation, SavedSearch
from rest_framework import serializers
from rest_framework.exceptions import ParseError
from tags.serializers import TagSerializer
from tags.models import Tag
from users.serializers import UserSerializer
from users.models import User
from project.models import Project
import simplejson as json
import logging


logger = logging.getLogger(__name__)


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
        return [ranges.__dict__]

    def to_internal_value(self, data):
        try:
            start = data[0]['start']
            end = data[0]['end']
            startOffset = data[0]['startOffset']
            endOffset = data[0]['endOffset']
            return Range(start, end, startOffset, endOffset)
        except AttributeError:
            logger.error("ranges array recieved malformed. Cannot convert to internal value")
            return AttributeError


class DatapointSerializer(serializers.ModelSerializer):
    # tags = TagSerializer(many=True, required=False)

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
        instance.tags = validated_data.get('tags', instance.tags)

        # Get all tags
        # If the tag doesn't have a slug (meaning it is an a new tag, and must be saved)
        # Create a new tag
        # Add it to the instance (How?)
        # instance.tags = None
        # for tag in validated_data['tags']:
        #     if 'id' not in tag:
        #         new_tag = Tag.objects.create(name=tag['name'])
        #         instance.tags.add(new_tag)
        #     else:
        #         instance.tags.add

        instance.save()
        return instance


class AnnotationSerializer(serializers.Serializer):
    id = serializers.CharField(label="id", required=False)
    annotator_schema_version = serializers.CharField(max_length=8, allow_blank=True, required=False)
    created = serializers.CharField(allow_blank=True, required=False)
    updated = serializers.CharField(source='modified', allow_blank=True, required=False)
    text = serializers.CharField()
    quote = serializers.CharField()
    uri = serializers.CharField(max_length=100, min_length=None, allow_blank=True, required=False)
    ranges = RangeSerializer()
    user = serializers.CharField(source='owner', label='user', required=False)
    tags = TagSerializer(many=True, required=False)
    datapoint = serializers.CharField()

    def update(self, instance, validated_data):
        instance.annotator_schema_version = validated_data.get('annotator_schema_version', instance.annotator_schema_version)
        instance.text = validated_data.get('text', instance.text)
        instance.quote = validated_data.get('quote', instance.quote)
        instance.uri = validated_data.get('uri', instance.uri)

        # Unpacking the ranges dict into 4 fields in instance.
        try:
            ranges = validated_data['ranges']
            instance.range_start = ranges.start
            instance.range_end = ranges.end
            instance.range_startOffset = ranges.startOffset
            instance.range_endOffset = ranges.endOffset
        except KeyError:
            logger.info("No ranges array passed to AnnotationSerializer.")

        instance.tags = validated_data.get('tags', instance.tags)

        instance.save()
        return instance

    def create(self, validated_data):
        annotation = dict()
        annotation['owner'] = self.context['request'].user
        annotation['quote'] = validated_data.get('quote')
        annotation['text'] = validated_data.get('text')
        annotation['uri'] = validated_data.get('uri')
        annotation['datapoint'] = Datapoint.objects.get(pk=validated_data.get('datapoint'))

        # Unpacking the ranges dict into 4 fields in instance.
        try:
            ranges = validated_data['ranges']
            annotation['range_start'] = ranges.start
            annotation['range_end'] = ranges.end
            annotation['range_startOffset'] = ranges.startOffset
            annotation['range_endOffset'] = ranges.endOffset
        except KeyError:
            logger.info("No ranges array passed to AnnotationSerializer.")

        return Annotation.objects.create(**annotation)


class SavedSearchSerializer(serializers.ModelSerializer):
    search_term = serializers.CharField(max_length=150)
    owner = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = SavedSearch

    def create(self, validated_data):
        savedsearch = dict()
        savedsearch['search_term'] = validated_data.get('search_term')
        savedsearch['owner'] = self.context['request'].user

        return SavedSearch.objects.create(**savedsearch)
