# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datapoint.models


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='file',
            field=models.FileField(upload_to=datapoint.models.datapoint_path, blank=True),
        ),
    ]
