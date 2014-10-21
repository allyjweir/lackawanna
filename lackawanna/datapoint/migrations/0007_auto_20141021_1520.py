# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datapoint', '0006_auto_20141021_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datapoint',
            name='file',
            field=models.FileField(upload_to=b'application_data/%Y/%m/%d', blank=True),
        ),
    ]
