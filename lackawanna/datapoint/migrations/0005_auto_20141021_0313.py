# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0004_auto_20141021_0312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='modified',
            field=models.DateTimeField(blank=True),
        ),
    ]
