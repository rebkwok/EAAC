# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0002_auto_20141115_1712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, to='timetable.Discipline'),
        ),
        migrations.AlterField(
            model_name='session',
            name='end_time',
            field=models.TimeField(verbose_name='end'),
        ),
        migrations.AlterField(
            model_name='session',
            name='level',
            field=models.CharField(blank=True, default='All levels', null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='session',
            name='location',
            field=models.ForeignKey(blank=True, null=True, to='timetable.Location'),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_date',
            field=models.DateField(verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='session',
            name='spaces',
            field=models.NullBooleanField(default=True, verbose_name='spaces available'),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_time',
            field=models.TimeField(verbose_name='start'),
        ),
    ]
