from django.db import models
from markupfield.fields import MarkupField


class Transcript(models.Model):
    datapoint = models.ForeignKey('datapoint.Datapoint', related_name='datapoint relation')
    creator = models.ForeignKey('users.User', related_name='creator relation')
    name = models.CharField(max_length=128)
    text = MarkupField(markup_type='markdown')

    # Created/Modified
    # See this for background: http://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
    created     = models.DateTimeField(editable = False)
    modified    = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        return super(Datapoint, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name