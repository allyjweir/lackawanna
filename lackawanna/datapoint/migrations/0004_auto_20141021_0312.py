# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0003_auto_20141021_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='annotations',
            field=models.ForeignKey(related_name=b'datapoint_annotations_relation', blank=True, to='annotate.Annotation', null=True),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='transcripts',
            field=models.ForeignKey(related_name=b'datapoint_transcripts_relation', blank=True, to='transcript.Transcript', null=True),
        ),
    ]
