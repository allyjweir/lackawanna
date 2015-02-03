# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0002_auto_20150114_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='range_end',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='range_start',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
