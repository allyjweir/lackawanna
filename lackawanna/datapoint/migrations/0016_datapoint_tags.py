# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0015_auto_20150114_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='tags',
            field=models.ManyToManyField(related_name=b'datapoint_tags_relation', to='datapoint.Tag', blank=True),
            preserve_default=True,
        ),
    ]
