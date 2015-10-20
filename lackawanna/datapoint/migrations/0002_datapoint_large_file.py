# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from s3direct.fields import S3DirectField

class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='large_file',
            field=S3DirectField(dest='all', blank=True),
            preserve_default=False,
        ),
    ]
