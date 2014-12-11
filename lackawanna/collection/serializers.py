from django.forms import widgets
from rest_framework import serializers
from collection.models import Collection


class CollectionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Collection
		fields = ('pk', 'owner', 'project', 'name', 'slug', 'description',)
