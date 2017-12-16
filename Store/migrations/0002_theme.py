# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 16:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=300, upload_to='zhuti/%Y/%m', verbose_name='主题')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '主题',
                'verbose_name_plural': '主题',
            },
        ),
    ]
