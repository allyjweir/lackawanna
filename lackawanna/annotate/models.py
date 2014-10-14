from django.db import models
from taggit.managers import TaggableManager


class Annotation(models.Model):
    datapoint = models.ForeignKey('datapoint.Datapoint', related_name='%(class)s_parent_datapoint_relation')
    owner = models.ForeignKey('users.User', related_name='%(class)s_creator_relation')

    # Key fields from the Annotator JSON Format: http://docs.annotatorjs.org/en/latest/annotation-format.html
    text = models.TextField(blank=True)
    quote = models.TextField()
    uri = models.URLField(blank=True)
    range_start = models.CharField(max_length=50)
    range_end = models.CharField(max_length=50)
    range_startOffset = models.BigIntegerField(blank=True)
    range_endOffset = models.BigIntegerField(blank=True)
    tags = TaggableManager(blank=True)

    # Created/Modified
    # See this for background:
    # http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    created = models.DateTimeField(editable = False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Datapoint, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.datapoint.name + ":'" + self.quote + "'"