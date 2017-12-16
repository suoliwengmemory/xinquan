# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 14:48
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='标题')),
                ('show', models.CharField(choices=[('yes', '显示'), ('qx', '不显示')], default='', max_length=3, verbose_name='首页显示')),
                ('image', models.ImageField(upload_to='fengmian/%Y/%m', verbose_name='封面')),
                ('image1', models.ImageField(upload_to='dianpu/%Y/%m', verbose_name='轮播图1')),
                ('image2', models.ImageField(upload_to='dianpu/%Y/%m', verbose_name='轮播图2')),
                ('image3', models.ImageField(upload_to='dianpu/%Y/%m', verbose_name='轮播图3')),
                ('image4', models.ImageField(upload_to='dianpu/%Y/%m', verbose_name='轮播图4')),
                ('image5', models.ImageField(upload_to='dianpu/%Y/%m', verbose_name='轮播图5')),
                ('detail', DjangoUeditor.models.UEditorField(default='', verbose_name='店铺内容')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '店铺',
                'verbose_name_plural': '店铺',
            },
        ),
    ]
