# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 19:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0002_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='image',
        ),
    ]
