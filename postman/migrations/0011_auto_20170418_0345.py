# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postman', '0010_sendingletters_from_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendingletters',
            name='from_message',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='postman.Tableofounemails'),
        ),
    ]