from django.db import models
from django_markdown.models import MarkdownField
from django.core.urlresolvers import reverse
import datetime


class Transcript(models.Model):
    datapoint = models.ForeignKey('datapoint.Datapoint', related_name='%(class)s_datapoint_relation')
    creator = models.ForeignKey('users.User', related_name='%(class)s_creator_relation')
    name = models.CharField(max_length=128)
    text = MarkdownField()

    # Created/Modified
    # See this for background:
    # http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Transcript, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('transcript:viewer', kwargs={'pk':self.pk})
