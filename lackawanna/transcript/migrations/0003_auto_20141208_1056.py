# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0002_auto_20141014_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcript',
            name='_text_rendered',
            field=models.TextField(default='cats', editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transcript',
            name='text_markup_type',
            field=models.CharField(default=None, max_length=30, choices=[(b'', b'--'), (b'markdown', b'markdown')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='transcript',
            name='text',
            field=markupfield.fields.MarkupField(),
        ),
    ]
