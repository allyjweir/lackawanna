from django.forms import ModelForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

from .models import Collection


class CollectionCreationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                ("Create a new collection"),
                'project',
                'name',
                'description',
                ),
            ButtonHolder(
                Submit('save', ('Create collection'), css_class='btn btn-primary pull-right'),
            )
        )
        super(CollectionCreationForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Collection
        fields = ['project', 'name', 'description']
