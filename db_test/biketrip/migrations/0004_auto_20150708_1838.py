# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biketrip', '0003_station_trip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='start_time',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='trip',
            name='stop_time',
            field=models.CharField(max_length=16),
        ),
    ]
