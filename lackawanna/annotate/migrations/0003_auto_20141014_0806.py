# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0002_auto_20141013_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='quote',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
