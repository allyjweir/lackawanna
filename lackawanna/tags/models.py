from django.db import models
from autoslug import AutoSlugField


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = AutoSlugField(populate_from='name', unique_with='name')

    def __unicode__(self):
        return self.name
