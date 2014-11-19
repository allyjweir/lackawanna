# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0012_auto_20141110_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datapoint',
            name='annotations',
        ),
        migrations.RemoveField(
            model_name='datapoint',
            name='transcripts',
        ),
        migrations.AddField(
            model_name='datapoint',
            name='related_datapoints',
            field=models.ManyToManyField(to='datapoint.Datapoint', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='filetype',
            field=models.CharField(default=b'file', max_length=5, blank=True, choices=[(b'file', b'File'), (b'video', b'Video'), (b'image', b'Image'), (b'pdf', b'PDF'), (b'text', b'Text'), (b'audio', b'Audio'), (b'web', b'Web')]),
        ),
    ]
