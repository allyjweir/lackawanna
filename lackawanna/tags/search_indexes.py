import datetime
from haystack import indexes
from .models import Tag


class TagIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Tag

    def get_model(self):
        return Tag

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
