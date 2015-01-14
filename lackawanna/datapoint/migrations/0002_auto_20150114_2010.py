# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0001_initial'),
        ('taggit', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0002_project_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='owner',
            field=models.ForeignKey(related_name=b'datapoint_uploader_relation', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datapoint',
            name='project',
            field=models.ForeignKey(related_name=b'datapoint_project_relation', to='project.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datapoint',
            name='related_datapoints',
            field=models.ManyToManyField(to='datapoint.Datapoint', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datapoint',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annotation',
            name='datapoint',
            field=models.ForeignKey(related_name=b'annotation_parent_datapoint_relation', to='datapoint.Datapoint'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annotation',
            name='owner',
            field=models.ForeignKey(related_name=b'annotation_creator_relation', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='annotation',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
