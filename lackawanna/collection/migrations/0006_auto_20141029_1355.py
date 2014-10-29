# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0005_auto_20141020_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='slug',
            field=autoslug.fields.AutoSlugField(unique=True, editable=False),
        ),
    ]
