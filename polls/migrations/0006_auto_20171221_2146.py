# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-21 16:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_comments_requests'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='requsted_to',
            new_name='requested_to',
        ),
    ]