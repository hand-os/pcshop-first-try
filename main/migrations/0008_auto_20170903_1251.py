# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170901_0925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notebook',
            old_name='CPU',
            new_name='property_1',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='RAM',
            new_name='property_2',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='video',
            new_name='property_3',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='memory',
            new_name='property_4',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='screen',
            new_name='property_5',
        ),
        migrations.RenameField(
            model_name='notebook',
            old_name='provider',
            new_name='property_6',
        ),
    ]