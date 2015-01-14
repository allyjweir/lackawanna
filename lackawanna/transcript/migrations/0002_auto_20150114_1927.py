# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('transcript', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('datapoint', '0002_auto_20150114_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcript',
            name='creator',
            field=models.ForeignKey(related_name=b'transcript_creator_relation', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='transcript',
            name='datapoint',
            field=models.ForeignKey(related_name=b'transcript_datapoint_relation', to='datapoint.Datapoint'),
            preserve_default=True,
        ),
    ]
