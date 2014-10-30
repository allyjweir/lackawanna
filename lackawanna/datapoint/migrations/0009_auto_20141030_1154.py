# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0008_datapoint_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
