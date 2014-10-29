from django import forms
from .models import Datapoint

class FileForm(forms.Form):
    file = forms.FileField(label='Upload a file')
class WebForm(forms.Form):
    url = forms.URLField(label='Link')

    class Meta:
        model = Datapoint
        fields = ('uploaded_by', 'name', 'url',)

    def process(self):
        #Do the work that needs done to the tweet here
        pass
    