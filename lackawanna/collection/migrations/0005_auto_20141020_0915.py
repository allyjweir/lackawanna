# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20141015_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False),
        ),
    ]
