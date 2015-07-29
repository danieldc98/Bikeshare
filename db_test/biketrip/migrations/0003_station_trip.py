# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('biketrip', '0002_auto_20150706_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('id_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('trip_id', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('stop_time', models.DateTimeField()),
                ('bike_id', models.IntegerField()),
                ('trip_duration_minutes', models.IntegerField()),
                ('from_station', models.ForeignKey(related_name='trip_from_station', to='biketrip.Station')),
                ('to_station', models.ForeignKey(related_name='trip_to_station', to='biketrip.Station')),
                ('user', models.ForeignKey(to='biketrip.Person')),
            ],
        ),
    ]
