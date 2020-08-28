# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170831_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='complecting',
            name='maincategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maincat1', to='main.BigCategory', verbose_name='Раздел'),
        ),
        migrations.AddField(
            model_name='notebook',
            name='maincategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maincat', to='main.BigCategory', verbose_name='Раздел'),
        ),
    ]
