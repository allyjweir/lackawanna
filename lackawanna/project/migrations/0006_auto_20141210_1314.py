# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20141020_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=model_utils.fields.StatusField(default=b'Public', max_length=100, no_check_for_status=True, choices=[(b'Public', b'Public'), (b'Private', b'Private')]),
        ),
    ]
