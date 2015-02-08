# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('slug', autoslug.fields.AutoSlugField(unique=True, editable=False)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
                ('owner', models.ForeignKey(related_name=b'collection_owner_relation', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(related_name=b'collection_project_relation', to='project.Project')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
