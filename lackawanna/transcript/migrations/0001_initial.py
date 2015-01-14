# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('text', django_markdown.models.MarkdownField()),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
