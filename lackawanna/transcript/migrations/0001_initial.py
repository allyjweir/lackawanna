# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('text', models.CharField(max_length=8192)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('creator', models.ForeignKey(related_name=b'transcript_creator_relation', to=settings.AUTH_USER_MODEL)),
                ('datapoint', models.ForeignKey(related_name=b'transcript_datapoint_relation', to='datapoint.Datapoint')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
