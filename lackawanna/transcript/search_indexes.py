import datetime
from haystack import indexes
from .models import Transcript


class TranscriptIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    owner = indexes.CharField(model_attr="owner")
    name = indexes.CharField(model_attr="name")
    body = indexes.CharField(model_attr="text")

    def get_model(self):
        return Transcript

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
