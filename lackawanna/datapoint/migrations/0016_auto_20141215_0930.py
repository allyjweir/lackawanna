# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0015_auto_20141215_0917'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datapoint',
            options={},
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='created',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='modified',
            field=models.DateTimeField(blank=True),
        ),
    ]
