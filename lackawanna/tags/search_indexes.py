import datetime
from haystack import indexes
from .models import Tag

class TagIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Tag
