from django.forms import widgets
from rest_framework import serializers
from tags.models import Tag


class TagSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug = serializers.CharField(required=False, allow_blank=True)
