# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('info', models.TextField(null=True, verbose_name='instructor description', blank=True)),
                ('photo', models.ImageField(null=True, help_text='Please upload a .jpg image with equal height and width', blank=True, upload_to='instructors')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
