# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 20:45
from __future__ import unicode_literals

from django.db import migrations, models
import stdimage.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('bio', tinymce.models.HTMLField()),
                ('image', stdimage.models.StdImageField(upload_to=b'')),
            ],
        ),
    ]
