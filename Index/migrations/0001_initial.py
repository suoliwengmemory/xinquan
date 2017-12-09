# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 14:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='shouye/%Y/%m', verbose_name='首页1')),
                ('image2', models.ImageField(upload_to='shouye/%Y/%m', verbose_name='首页2')),
                ('image3', models.ImageField(upload_to='shouye/%Y/%m', verbose_name='首页3')),
                ('image4', models.ImageField(upload_to='shouye/%Y/%m', verbose_name='首页4')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '首页',
                'verbose_name_plural': '首页',
            },
        ),
    ]