# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 10:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('postman', '0009_auto_20170418_0040'),
    ]

    operations = [
        migrations.AddField(
            model_name='sendingletters',
            name='from_message',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='postman.Whoarewe'),
        ),
    ]