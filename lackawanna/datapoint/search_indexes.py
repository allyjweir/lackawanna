import datetime
from haystack import indexes
from .models import Datapoint

class DatapointIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    owner = indexes.CharField(model_attr='owner')
    name = indexes.CharField(model_attr='name')
    filetype = indexes.CharField(model_attr='filetype')
    description = indexes.CharField(model_attr='description')

    def get_model(self):
        return Datapoint

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
