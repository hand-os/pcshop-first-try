# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-24 11:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20171124_0903'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoPack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d/', verbose_name='Изображение')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.BigCategory', verbose_name='Категория')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='productstat',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 11, 24, 11, 37, 40, 751741, tzinfo=utc), verbose_name='Дата'),
        ),
        migrations.AddField(
            model_name='hubnotebook',
            name='image_array',
            field=models.ManyToManyField(blank=True, null=True, to='main.PhotoPack'),
        ),
        migrations.AlterIndexTogether(
            name='photopack',
            index_together=set([('id',)]),
        ),
    ]
