# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-27 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_remove_likes_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='likes',
            name='liked_by_name',
            field=models.CharField(default='user', max_length=150),
        ),
        migrations.AddField(
            model_name='likes',
            name='liked_post_title',
            field=models.CharField(default='post', max_length=100),
        ),
    ]
