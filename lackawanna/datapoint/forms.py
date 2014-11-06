from django import forms
from .models import Datapoint

from web_processing import process_website


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


class WebForm(forms.Form):
    url = forms.URLField(label='Link')

    class Meta:
        model = Datapoint
        fields = ('uploaded_by', 'name', 'url', 'description', 'author', 'source', 'publish_date',)

    def process_web(self):
        print ("Made it back to WebForm")
        return process_website(self.cleaned_data['url'])
