# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 22:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20160426_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Employee'),
        ),
    ]