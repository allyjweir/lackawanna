from django.db import models
from taggit.managers import TaggableManager
import datetime

class Datapoint(models.Model):
    # Relationships
    uploaded_by = models.ForeignKey('users.User', related_name='%(class)s_uploader_relation')
    project = models.ForeignKey('project.Project', related_name='%(class)s_project_relation')
    collections = models.ManyToManyField('collection.Collection', related_name='%(class)s_collection_relation',
                                         blank=True)

    # File management
    name = models.CharField(max_length=512)
    filetype = models.CharField(max_length=20, blank=True)
    file = models.FileField(upload_to='application_data/%Y/%m/%d', blank=True)

    # Descriptive metadata
    description = models.TextField(blank=True)
    author = models.CharField(max_length=256, blank=True)
    source = models.CharField(max_length=256, blank=True)
    url = models.URLField(blank=True)
    publish_date = models.DateField(null=True, blank=True)

    # User created metadata
    tags = TaggableManager(blank=True)
    annotations = models.ForeignKey('annotate.Annotation', related_name='%(class)s_annotations_relation', blank=True,
                                    null=True)
    transcripts = models.ForeignKey('transcript.Transcript', related_name='%(class)s_transcripts_relation', blank=True,
                                    null=True)

    # Created/Modified
    # See this for background:
    # http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Datapoint, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name