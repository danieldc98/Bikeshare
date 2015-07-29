# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biketrip', '0005_trip_google_duration_minutes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='google_duration_minutes',
            field=models.IntegerField(),
        ),
    ]
