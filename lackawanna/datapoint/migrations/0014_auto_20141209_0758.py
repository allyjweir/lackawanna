# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0013_auto_20141119_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='datapoint',
            old_name='uploaded_by',
            new_name='owner',
        ),
    ]
