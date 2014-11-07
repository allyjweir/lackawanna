# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0010_auto_20141105_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='file_extension',
            field=models.CharField(default='', max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
