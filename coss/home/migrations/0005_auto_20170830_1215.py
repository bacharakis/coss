# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 12:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_aboutsnippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutsnippet',
            name='bottom_cta1_link',
            field=models.URLField(blank=True, default='', verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='aboutsnippet',
            name='bottom_cta1_text',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='aboutsnippet',
            name='bottom_cta2_link',
            field=models.URLField(blank=True, default='', verbose_name='Link'),
        ),
        migrations.AddField(
            model_name='aboutsnippet',
            name='bottom_cta2_text',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='aboutsnippet',
            name='bottom_cta_text',
            field=models.CharField(blank=True, default='', max_length=40, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='aboutsnippet',
            name='bottom_cta_title',
            field=models.CharField(blank=True, default='', max_length=40, verbose_name='Title'),
        ),
        migrations.AddField(
            model_name='aboutsnippet',
            name='title',
            field=models.CharField(default='', max_length=40),
        ),
    ]
