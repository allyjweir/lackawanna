# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0002_auto_20141013_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='annotations',
            field=models.ForeignKey(related_name=b'datapoint_annotations_relation', blank=True, to='annotate.Annotation'),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='collections',
            field=models.ManyToManyField(related_name=b'datapoint_collection_relation', to=b'collection.Collection', blank=True),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='transcripts',
            field=models.ForeignKey(related_name=b'datapoint_transcripts_relation', blank=True, to='transcript.Transcript'),
        ),
    ]
