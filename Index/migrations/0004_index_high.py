# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0003_auto_20171208_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='high',
            field=models.CharField(default='', max_length=30, verbose_name='图片高度'),
            preserve_default=False,
        ),
    ]
