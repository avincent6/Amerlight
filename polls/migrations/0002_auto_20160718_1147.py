# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-18 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudie',
            name='pdf_link',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='casestudie',
            name='video_link',
            field=models.CharField(default=0, max_length=150),
            preserve_default=False,
        ),
    ]
