from django.forms import ModelForm
from django import forms
from .models import Datapoint

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

from s3direct.widgets import S3DirectWidget

class DatapointLargeFileUploadForm(ModelForm):
    large_file = forms.URLField(widget=S3DirectWidget(dest='all'))

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                ("Upload a Video/Audio Datapoint"),
                'project',
                'name',
                'filetype'
                'large_file',
                'description',
                'author',
                'source',
                'url',
                ),
            ButtonHolder(
                Submit('save', ('Upload datapoint'), css_class='btn btn-primary pull-right'),
            )
        )
        super(DatapointVideoUploadForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Datapoint
        fields = ('project', 'name', 'filetype', 'large_file', 'description', 'author', 'source', 'url',)

class DatapointFileUploadForm(ModelForm):
    file = forms.FileField()

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                ("Upload a file Datapoint"),
                'project',
                'name',
                'file',
                'description',
                'author',
                'source',
                'url',
                ),
            ButtonHolder(
                Submit('save', ('Upload datapoint'), css_class='btn btn-primary pull-right'),
            )
        )
        super(DatapointFileUploadForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Datapoint
        fields = ('project', 'name', 'file', 'description', 'author', 'source', 'url',)


class DatapointWebRetrievalForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                ("Retrieve an online resource"),
                Field('project'),
                Field('url', title='URL', label='URL'),
            ),
            ButtonHolder(
                Submit('save', ('Retrieve datapoint'), css_class='btn btn-primary pull-right'),
            )
        )
        super(DatapointWebRetrievalForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Datapoint
        fields = ('url', 'project',)
