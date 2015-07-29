# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biketrip', '0004_auto_20150708_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='google_duration_minutes',
            field=models.IntegerField(default=0),
        ),
    ]
