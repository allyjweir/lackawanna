from django.db import models
from markupfield.fields import MarkupField
from model_utils.fields import StatusField
from model_utils import Choices
import datetime

class Project(models.Model):
    owner = models.ForeignKey('users.User', related_name='owner_relation')
    name = models.CharField(max_length = 128, unique=True)
    description = MarkupField(markup_type='markdown')
    website = models.URLField(blank=true)

    # If accessible to everyone or only owner
    STATUS = Choices('public', 'private')
    status = StatusField()

    # See this for background: http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    created     = models.DateTimeField(editable=False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Project, self).save(*args, **kwargs)

    def __unicode__ (self):
        return self.name
