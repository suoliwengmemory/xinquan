# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 22:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Goods', '0003_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(default='', max_length=100, verbose_name='产品种类')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '产品种类',
                'verbose_name_plural': '产品种类',
            },
        ),
        migrations.DeleteModel(
            name='Type',
        ),
    ]
