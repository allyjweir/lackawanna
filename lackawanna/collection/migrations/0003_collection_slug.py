# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0002_auto_20141014_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='slug',
            field=models.SlugField(default=datetime.date(2014, 10, 15)),
            preserve_default=False,
        ),
    ]
