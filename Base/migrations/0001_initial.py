# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 16:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar1', models.CharField(max_length=50, verbose_name='导航栏一')),
                ('bar2', models.CharField(max_length=50, verbose_name='导航栏二')),
                ('bar3', models.CharField(max_length=50, verbose_name='导航栏三')),
                ('bar4', models.CharField(max_length=50, verbose_name='导航栏四')),
                ('bar5', models.CharField(max_length=50, verbose_name='导航栏五')),
                ('bar6', models.CharField(max_length=50, verbose_name='导航栏六')),
                ('bar7', models.CharField(max_length=50, verbose_name='导航栏七')),
                ('image', models.ImageField(max_length=50, upload_to='tabbar/%Y/%m', verbose_name='LOGO')),
                ('Telephone', models.CharField(max_length=30, verbose_name='联系电话')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '首部导航栏',
                'verbose_name_plural': '首部导航栏',
            },
        ),
        migrations.CreateModel(
            name='Side',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar', models.CharField(max_length=50, verbose_name='首页导航')),
                ('bar1', models.CharField(max_length=50, verbose_name='导航栏一')),
                ('bar2', models.CharField(max_length=50, verbose_name='导航栏二')),
                ('bar3', models.CharField(max_length=50, verbose_name='导航栏三')),
                ('bar4', models.CharField(max_length=50, verbose_name='导航栏四')),
                ('bar5', models.CharField(max_length=50, verbose_name='导航栏五')),
                ('bar6', models.CharField(max_length=50, verbose_name='导航栏六')),
                ('bar7', models.CharField(max_length=50, verbose_name='导航栏七')),
                ('Telephone', models.CharField(max_length=30, verbose_name='联系电话')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '左部导航栏',
                'verbose_name_plural': '左部导航栏',
            },
        ),
        migrations.CreateModel(
            name='Tabbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bar1', models.CharField(max_length=50, verbose_name='导航栏一')),
                ('bar2', models.CharField(max_length=50, verbose_name='导航栏二')),
                ('bar3', models.CharField(max_length=50, verbose_name='导航栏三')),
                ('bar4', models.CharField(max_length=50, verbose_name='导航栏四')),
                ('bar5', models.CharField(max_length=50, verbose_name='导航栏五')),
                ('bar6', models.CharField(max_length=50, verbose_name='导航栏六')),
                ('image', models.ImageField(upload_to='tabbar/%Y/%m', verbose_name='二维码')),
                ('Telephone', models.CharField(max_length=30, verbose_name='联系电话')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '底部导航栏',
                'verbose_name_plural': '底部导航栏',
            },
        ),
    ]