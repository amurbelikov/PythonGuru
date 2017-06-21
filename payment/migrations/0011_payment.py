# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-14 10:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_auto_20161114_1016'),
        ('payment', '0010_auto_20161101_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('invoice_id', models.CharField(default=uuid.uuid4, max_length=100, unique=True)),
                ('stripe_reference', models.CharField(blank=True, max_length=40)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('credits_used', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('details', jsonfield.fields.JSONField(default=dict)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='account.Account')),
            ],
        ),
    ]
