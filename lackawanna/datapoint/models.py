from django.db import models
from taggit.managers import TaggableManager
import datetime

class Datapoint(models.Model):
    # Relationships
    owner = models.ForeignKey('users.User', related_name='%(class)s_uploader_relation')
    project = models.ForeignKey('project.Project', related_name='%(class)s_project_relation')
    collections = models.ManyToManyField('collection.Collection', related_name='%(class)s_collection_relation',
                                         blank=True)
    tags = models.ManyToManyField('Tag', related_name='%(class)s_tags_relation', blank=True)

    # File management
    name = models.CharField(max_length=512)
    file = models.FileField(upload_to='application_data/%Y/%m/%d', blank=True)
    filename = models.CharField(max_length=512, blank=True)
    file_extension = models.CharField(max_length=100, blank=True)

    #Filetypes
    FILE = 'file'
    VIDEO = 'video'
    IMAGE = 'image'
    PDF = 'pdf'
    TEXT = 'text'
    AUDIO = 'audio'
    WEB = 'web'
    FILETYPE_CHOICES = (
        (FILE, 'File'),
        (VIDEO, 'Video'),
        (IMAGE, 'Image'),
        (PDF, 'PDF'),
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (WEB, 'Web'),)
    filetype = models.CharField(
        max_length=5,
        choices=FILETYPE_CHOICES,
        default=FILE,
        blank=True)
    filesize = models.CharField(max_length=256, blank=True)


    # Descriptive metadata
    description = models.TextField(blank=True)
    author = models.CharField(max_length=256, blank=True)
    source = models.CharField(max_length=256, blank=True)
    url = models.URLField(blank=True)
    publish_date = models.DateField(null=True, blank=True)
    related_datapoints = models.ManyToManyField('self', symmetrical=False, null=True, blank=True)

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

class Tag(models.Model):
    name = models.CharField(primary_key=True, max_length=512)

    def __unicode__(self):
        return self.name
