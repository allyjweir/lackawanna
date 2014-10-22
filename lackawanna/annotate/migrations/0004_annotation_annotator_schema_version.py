# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0003_auto_20141014_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotation',
            name='annotator_schema_version',
            field=models.CharField(default='v1.0', max_length=8, blank=True),
            preserve_default=False,
        ),
    ]
