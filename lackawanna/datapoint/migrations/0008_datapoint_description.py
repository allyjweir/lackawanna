# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0007_auto_20141021_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='description',
            field=models.TextField(default='cat'),
            preserve_default=False,
        ),
    ]
