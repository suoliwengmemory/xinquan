# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lesson', '0002_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='image',
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=30, verbose_name='课程'),
        ),
    ]
