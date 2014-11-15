# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_time',
            field=models.TimeField(verbose_name='end time'),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_date',
            field=models.DateField(verbose_name='session date'),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_time',
            field=models.TimeField(verbose_name='start time'),
        ),
    ]
