# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0014_auto_20141209_0758'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datapoint',
            options={'ordering': ('-modified', '-created'), 'get_latest_by': 'modified'},
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='datapoint',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True),
        ),
    ]
