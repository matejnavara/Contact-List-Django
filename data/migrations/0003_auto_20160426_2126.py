# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-26 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20160426_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Department'),
        ),
    ]
