# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-08 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=2)),
                ('image', models.CharField(max_length=255)),
                ('cleanPhone', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
