# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gluu_license', '0016_auto_20161117_2011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='creation_date',
            field=models.DateTimeField(),
        ),
    ]
