# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 14:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discourse', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discoursecategory',
            name='name',
        ),
    ]