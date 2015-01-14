# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('annotator_schema_version', models.CharField(max_length=8, blank=True)),
                ('text', models.TextField(blank=True)),
                ('quote', models.TextField()),
                ('uri', models.URLField(blank=True)),
                ('range_start', models.CharField(max_length=50)),
                ('range_end', models.CharField(max_length=50)),
                ('range_startOffset', models.BigIntegerField()),
                ('range_endOffset', models.BigIntegerField()),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Datapoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512)),
                ('file', models.FileField(upload_to=b'application_data/%Y/%m/%d', blank=True)),
                ('filename', models.CharField(max_length=512, blank=True)),
                ('file_extension', models.CharField(max_length=100, blank=True)),
                ('filetype', models.CharField(default=b'file', max_length=5, blank=True, choices=[(b'file', b'File'), (b'video', b'Video'), (b'image', b'Image'), (b'pdf', b'PDF'), (b'text', b'Text'), (b'audio', b'Audio'), (b'web', b'Web')])),
                ('filesize', models.CharField(max_length=256, blank=True)),
                ('description', models.TextField(blank=True)),
                ('author', models.CharField(max_length=256, blank=True)),
                ('source', models.CharField(max_length=256, blank=True)),
                ('url', models.URLField(blank=True)),
                ('publish_date', models.DateField(null=True, blank=True)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(blank=True)),
                ('collections', models.ManyToManyField(related_name=b'datapoint_collection_relation', to='collection.Collection', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
