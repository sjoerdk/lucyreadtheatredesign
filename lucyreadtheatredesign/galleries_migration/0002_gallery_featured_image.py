# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 23:29
from __future__ import unicode_literals

from django.db import migrations
import mezzanine.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='featured_image',
            field=mezzanine.core.fields.FileField(blank=True, max_length=255, null=True, verbose_name='Header image'),
        ),
    ]
