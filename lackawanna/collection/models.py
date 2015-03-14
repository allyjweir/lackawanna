from django.db import models
from autoslug import AutoSlugField
from django.core.urlresolvers import reverse
import datetime


class Collection(models.Model):
    owner = models.ForeignKey('users.User', related_name='%(class)s_owner_relation')
    project = models.ForeignKey('project.Project', related_name='%(class)s_project_relation')
    name = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='name', unique=True)
    description = models.TextField(blank=True)

    # See this for background:
    # http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        # On save, update timestamps
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Collection, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.project.name + ":" + self.name

    def get_absolute_url(self):
        return reverse('collection:detail', kwargs={'slug': self.slug})
