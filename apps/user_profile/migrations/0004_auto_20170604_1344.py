# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-06-04 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_profile_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='ip',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
    ]
