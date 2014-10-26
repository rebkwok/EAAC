# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('info', models.TextField(null=True, verbose_name='session description')),
                ('photo', models.ImageField(null=True, upload_to='sessions', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('room', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('level', models.CharField(max_length=255, default='All levels')),
                ('session_date', models.DateTimeField(verbose_name='session date')),
                ('start_time', models.DateTimeField(verbose_name='start time')),
                ('end_time', models.DateTimeField(verbose_name='end time')),
                ('session_type', models.CharField(choices=[('CLASS', 'Class'), ('REGISTRATION', 'Registration'), ('WARMUP', 'Warm Up'), ('COOLDOWN', 'Cool Down'), ('BREAK', 'Break'), ('SHOW', 'Show')], max_length=12, default='CLASS')),
                ('spaces', models.BooleanField(verbose_name='spaces available', default=True)),
                ('discipline', models.ForeignKey(to='timetable.Discipline')),
                ('instructor', models.ForeignKey(null=True, to='instructors.Instructor', blank=True)),
                ('location', models.ForeignKey(to='timetable.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
