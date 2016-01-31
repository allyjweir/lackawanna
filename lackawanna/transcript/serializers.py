from django.forms import widgets
from rest_framework import serializers
from .models import Transcript


class TranscriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcript
        fields = ('pk', 'datapoint', 'owner', 'name', 'text')
