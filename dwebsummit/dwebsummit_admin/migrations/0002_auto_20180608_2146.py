# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-08 21:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dwebsummit_admin', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'verbose_name_plural': 'people'},
        ),
        migrations.AddField(
            model_name='person',
            name='type',
            field=models.CharField(blank=True, default='Participant', max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='organization',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='person',
            name='title',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]