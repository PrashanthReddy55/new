# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-28 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0015_remove_likes_liked_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='liked_post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_pooost', to='polls.Posts'),
        ),
    ]
