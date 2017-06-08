# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-28 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('data_of_birth', models.DateField()),
                ('biography', models.CharField(max_length=250)),
                ('contacts', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
