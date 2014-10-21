# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0005_auto_20141021_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='publish_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
