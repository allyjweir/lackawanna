from django.forms import widgets
from rest_framework import serializers
from project.models import Project

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('owner', 'name', 'slug', 'description', 'website', 'status')
