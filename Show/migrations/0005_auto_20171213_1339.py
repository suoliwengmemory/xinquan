# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 13:39
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Show', '0004_auto_20171213_1053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='title1',
        ),
        migrations.AddField(
            model_name='theme',
            name='detail',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='课程章节'),
        ),
    ]