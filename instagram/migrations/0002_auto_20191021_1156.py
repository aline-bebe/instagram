# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-21 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='pictures/'),
        ),
    ]
