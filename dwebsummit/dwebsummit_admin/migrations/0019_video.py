# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-15 22:50
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('dwebsummit_admin', '0018_auto_20180720_0045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='The title of the video. Will also be used to generate the URL.', max_length=255, unique=True)),
                ('page_url', models.CharField(db_index=True, editable=False, help_text='This URL is generated from the title', max_length=255, unique=True)),
                ('archive_identifier', models.CharField(help_text='Used to embed the video. eg. dweb-8_1_18_Front_End_Storiesfromthefield', max_length=255)),
                ('thumbnail', stdimage.models.StdImageField(blank=True, null=True, upload_to=b'')),
                ('body_text', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='')),
                ('is_featured', models.BooleanField(default=True, help_text='Will be shown at top of page')),
                ('people', models.ManyToManyField(blank=True, to='dwebsummit_admin.Person')),
                ('related_pages', models.ManyToManyField(blank=True, to='dwebsummit_admin.Page')),
            ],
            options={
                'verbose_name_plural': 'videos',
            },
        ),
    ]
