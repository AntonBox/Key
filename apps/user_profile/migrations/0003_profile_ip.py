# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-30 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20170529_1425'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='ip',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]