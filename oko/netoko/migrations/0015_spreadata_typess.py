# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 12:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netoko', '0014_auto_20170322_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='spreadata',
            name='typess',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='netoko.Typeofsocialnetwork'),
        ),
    ]