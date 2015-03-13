# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datapoint.models


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0004_auto_20150303_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='file',
            field=models.FileField(max_length=255, upload_to=datapoint.models.datapoint_path, blank=True),
        ),
    ]
