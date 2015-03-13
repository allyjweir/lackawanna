# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0003_savedsearch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='file_extension',
            field=models.CharField(max_length=512, blank=True),
        ),
    ]
