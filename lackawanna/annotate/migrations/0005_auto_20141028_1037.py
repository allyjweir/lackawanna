# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('annotate', '0004_annotation_annotator_schema_version'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annotation',
            name='modified',
            field=models.DateTimeField(editable=False),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='range_endOffset',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='annotation',
            name='range_startOffset',
            field=models.BigIntegerField(),
        ),
    ]
