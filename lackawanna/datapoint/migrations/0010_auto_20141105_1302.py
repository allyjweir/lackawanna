# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0009_auto_20141030_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='filename',
            field=models.CharField(default='piiza.txe', max_length=512, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datapoint',
            name='filesize',
            field=models.CharField(default=10, max_length=256, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='filetype',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
