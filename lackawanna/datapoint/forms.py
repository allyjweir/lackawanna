from django import forms
from .models import Datapoint

class FileForm(forms.Form):
    file = forms.FileField(label='Upload a file')

    class Meta:
        model = Datapoint
        fields = ('uploaded_by', 'name', 'file', 'filetype')