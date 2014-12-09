from django.forms import widgets
from rest_framework import serializers
from datapoint.models import Datapoint

class DatapointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Datapoint
		fields = ('pk', 'owner', 'project', 'collections', 'name', 'description', 'author', 'source', 'url', 'publish_date')
