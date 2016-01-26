# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0002_datapoint_large_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='filetype',
            field=models.CharField(default=b'file', max_length=256, blank=True, choices=[(b'file', b'File'), (b'video', b'Video'), (b'image', b'Image'), (b'pdf', b'PDF'), (b'text', b'Text'), (b'audio', b'Audio'), (b'web', b'Web')]),
        ),
    ]
