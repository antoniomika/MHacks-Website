# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-02 19:13
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MHacks', '0038_auto_20170202_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentorapplication',
            name='user_focused_design_skills',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, choices=[(b'User experience research', b'User experience research'), (b'Interaction design', b'Interaction design'), (b'Graphic design', b'Graphic design'), (b'Product design', b'Product design'), (b'Design thinking', b'Design thinking')], max_length=32), size=5),
        ),
    ]