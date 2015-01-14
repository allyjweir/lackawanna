# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('slug', autoslug.fields.AutoSlugField(editable=False)),
                ('description', models.TextField()),
                ('website', models.URLField(blank=True)),
                ('status', model_utils.fields.StatusField(default=b'Public', max_length=100, no_check_for_status=True, choices=[(b'Public', b'Public'), (b'Private', b'Private')])),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
