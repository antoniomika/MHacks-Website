# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-15 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MHacks', '0006_auto_20160815_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='race',
            field=models.CharField(default='', max_length=64),
        ),
    ]
