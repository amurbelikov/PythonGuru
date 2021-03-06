# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 19:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20161030_1956'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecommerceuser',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='billing_admins', to='account.Account'),
        ),
        migrations.AlterField(
            model_name='account',
            name='primary_contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='primary_account', to=settings.AUTH_USER_MODEL),
        ),
    ]
