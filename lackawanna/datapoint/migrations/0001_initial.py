# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('collection', '0001_initial'),
        ('annotate', '0001_initial'),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datapoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('filetype', models.CharField(max_length=20, blank=True)),
                ('file', models.FileField(upload_to=b'application_data/%Y/%m/%d')),
                ('author', models.CharField(max_length=256, blank=True)),
                ('source', models.CharField(max_length=256, blank=True)),
                ('url', models.URLField(blank=True)),
                ('publish_date', models.DateField(blank=True)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('annotations', models.ForeignKey(related_name=b'datapoint_annotations_relation', to='annotate.Annotation')),
                ('collections', models.ManyToManyField(related_name=b'datapoint_collection_relation', to='collection.Collection')),
                ('project', models.ForeignKey(related_name=b'datapoint_project_relation', to='project.Project')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
