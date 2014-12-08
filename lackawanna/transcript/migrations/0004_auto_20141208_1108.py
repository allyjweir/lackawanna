# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0003_auto_20141208_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transcript',
            name='_text_rendered',
        ),
        migrations.RemoveField(
            model_name='transcript',
            name='text_markup_type',
        ),
        migrations.AlterField(
            model_name='transcript',
            name='text',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
