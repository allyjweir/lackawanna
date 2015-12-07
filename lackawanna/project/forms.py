from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

from .models import Project


class ProjectCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                ("Create a new project"),
                'name',
                'description',
                'website',
                ),
            ButtonHolder(
                Submit('save', ('Create project'), css_class='btn btn-primary pull-right'),
            )
        )
        super(ProjectCreationForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Project
        fields = ['name', 'description', 'website']

class ProjectUpdateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                ("Update existing project"),
                'owner',
                'name',
                'description',
                'website',
                'status'
                ),
            ButtonHolder(
                Submit('save', ('Update project'), css_class='btn btn-primary pull-right'),
            )
        )
        super(ProjectUpdateForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Project
        fields = ['owner', 'name', 'description', 'website', 'status']
