# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-12 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0005_index_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='index',
            name='image',
            field=models.ImageField(null=True, upload_to='shouye/%Y/%m', verbose_name='封面'),
        ),
        migrations.AlterField(
            model_name='index',
            name='url',
            field=models.URLField(default='', max_length=100, null=True, verbose_name='链接地址'),
        ),
    ]
