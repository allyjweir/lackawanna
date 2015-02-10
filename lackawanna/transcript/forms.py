from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

from .models import Transcript


class TranscriptCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                ("Create a transcript"),
                'datapoint',
                'name',
                Field('text', data_provide="markdown", rows="25"),
                ),
            ButtonHolder(
                Submit('save', ('Create transcript'), css_class='btn btn-primary pull-right'),
            )
        )
        super(TranscriptCreationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Transcript
        fields = ['datapoint', 'name', 'text']


class TranscriptUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                ("Edit transcript"),
                'name',
                Field('text', data_provide="markdown", rows="25"),
                ),
            ButtonHolder(
                Submit('save', ('Update transcript'), css_class='btn btn-primary pull-right'),
            )
        )
        super(TranscriptUpdateForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Transcript
        fields = ['name', 'text']
