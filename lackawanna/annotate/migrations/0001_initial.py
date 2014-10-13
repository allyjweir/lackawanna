# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annotation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=99999, blank=True)),
                ('quote', models.CharField(max_length=99999)),
                ('uri', models.URLField(blank=True)),
                ('range_start', models.CharField(max_length=50)),
                ('range_end', models.CharField(max_length=50)),
                ('range_startOffset', models.BigIntegerField(blank=True)),
                ('range_endOffset', models.BigIntegerField(blank=True)),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
