from django import forms
from .models import Datapoint

import web_import


class FileForm(forms.Form):
    name = forms.CharField(label='Name', max_length=128)
    file = forms.FileField(label='Browse to File')
    description = forms.CharField(label='Description')
    author = forms.CharField(label='Author', max_length=256,)
    source = forms.CharField(label='Source', max_length=256,)
    url = forms.URLField(label='URL',)
    publish_date = forms.DateField()

    def process(self):
        print("Hello from the form!!!!")
        pass

    class Meta:
        model = Datapoint
        fields = ('name', 'file', 'description', 'author', 'source', 'url', 'publish_date', 'uploaded_by',)


class WebForm(forms.ModelForm):
    url = forms.URLField(label='Link')

    class Meta:
        model = Datapoint
        fields = ('url', 'project',)