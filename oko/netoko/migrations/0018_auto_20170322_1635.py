# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-22 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netoko', '0017_auto_20170322_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_country', models.CharField(max_length=50)),
                ('coordinates', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='botinfos',
            name='city_of_bot',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='netoko.Cities'),
        ),
    ]