# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import markupfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0003_savedsearch'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transcript',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('text', markupfield.fields.MarkupField()),
                ('created', models.DateTimeField(editable=False)),
                ('text_markup_type', models.CharField(default=b'markdown', max_length=30, editable=False, choices=[(b'', b'--'), (b'markdown', b'markdown')])),
                ('_text_rendered', models.TextField(editable=False)),
                ('modified', models.DateTimeField()),
                ('datapoint', models.ForeignKey(related_name=b'transcript_datapoint_relation', to='datapoint.Datapoint')),
                ('owner', models.ForeignKey(related_name=b'transcript_creator_relation', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
