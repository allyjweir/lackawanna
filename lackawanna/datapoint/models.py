from django.db import models
from django.core.urlresolvers import reverse
import datetime
from s3direct.fields import S3DirectField


def datapoint_path(self, filename):
    url = "datapoints/projects/%s/%s" % (self.project.slug, filename)
    return url


class Datapoint(models.Model):
    # Relationships
    owner = models.ForeignKey('users.User', related_name='%(class)s_uploader_relation')
    project = models.ForeignKey('project.Project', related_name='%(class)s_project_relation')
    collections = models.ManyToManyField('collection.Collection', related_name='%(class)s_collection_relation',
                                         blank=True)
    tags = models.ManyToManyField('tags.Tag', related_name="%(class)s_tags_relation", blank=True)

    # File management
    name = models.CharField(max_length=512)
    file = models.FileField(upload_to=datapoint_path, max_length=255, blank=True)

    """" large_file - Added to support direct upload to S3 for certain large file types that timeout during upload when hosted on Heroku. Has its own form and view for uploads and different references in the datapoint_detail.html template but otherwise treated the same"""
    large_file = S3DirectField(dest='all', blank=True)
    filename = models.CharField(max_length=512, blank=True)
    file_extension = models.CharField(max_length=512, blank=True)

    # Filetypes
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

    # Delete related file to datapoint
    def delete(self, *args, **kwargs):
        self.file.delete(False)
        return super(Datapoint, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('datapoint:viewer', args=[str(self.pk)])

    def __unicode__(self):
        return self.name


class Annotation(models.Model):
    datapoint = models.ForeignKey('datapoint.Datapoint', related_name='%(class)s_parent_datapoint_relation')
    owner = models.ForeignKey('users.User', related_name='%(class)s_creator_relation')
    tags = models.ManyToManyField('tags.Tag', related_name="%(class)s_tags_relation", blank=True)

    # Key fields from the Annotator JSON Format: http://docs.annotatorjs.org/en/latest/annotation-format.html
    annotator_schema_version = models.CharField(max_length=8, blank=True)
    text = models.TextField(blank=True)
    quote = models.TextField()
    uri = models.CharField(max_length=100, blank=True)
    range_start = models.CharField(max_length=50, blank=True)
    range_end = models.CharField(max_length=50, blank=True)
    range_startOffset = models.BigIntegerField()
    range_endOffset = models.BigIntegerField()

    # Created/Modified
    # See this for background:
    # http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Annotation, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.datapoint.name + ":'" + self.quote + "'"

    def ranges(self):
        return [self.range_start, self.range_end, self.range_startOffset, self.range_endOffset]


class SavedSearch(models.Model):
    search_term = models.CharField(max_length=150)
    owner = models.ForeignKey('users.User', related_name='%(class)s_creator_relation')

    def __unicode__(self):
        return self.search_term + " searched by: " + self.owner.username

    def get_absolute_url(self):
        return reverse('search', args=[str(self.search_term)])
