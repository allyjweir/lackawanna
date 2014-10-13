# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0001_initial'),
        ('transcript', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='datapoint',
            name='transcripts',
            field=models.ForeignKey(related_name=b'datapoint_transcripts_relation', to='transcript.Transcript'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='datapoint',
            name='uploaded_by',
            field=models.ForeignKey(related_name=b'datapoint_uploader_relation', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
