# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-15 21:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0002_auto_20170115_2134'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episode',
            options={'ordering': ['created_at']},
        ),
    ]