from django import forms
from haystack.forms import SearchForm

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

class LackawannaSearchForm(SearchForm):
    query = forms.CharField(label='Query')

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-10'
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
            Fieldset(
                ('Search'),
                'query',
            ),
            ButtonHolder(
                Submit('search', ('Search'), css_class='btn btn-primary'),
            )
        )


    def search(self):
        # First, store the SearchQuerySet received from other processing.
        sqs = super(LackawannaSearchForm, self).search()

        if not self.is_valid():
            return self.no_query_found()

        return sqs
