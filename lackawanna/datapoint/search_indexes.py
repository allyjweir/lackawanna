import datetime
from haystack import indexes
from .models import Datapoint, Annotation

class DatapointIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    owner = indexes.CharField(model_attr='owner')
    name = indexes.CharField(model_attr='name')
    filetype = indexes.CharField(model_attr='filetype')
    description = indexes.CharField(model_attr='description')
    source = indexes.CharField(model_attr="source")

    def get_model(self):
        return Datapoint

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class AnnotationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    annotation_text = indexes.CharField(model_attr="text")
    quote = indexes.CharField(model_attr="quote")
    owner = indexes.CharField(model_attr='owner')
    datapoint = indexes.CharField(model_attr='datapoint')

    def get_model(self):
        return Annotation

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
