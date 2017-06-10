# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 05:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netoko', '0007_auto_20170317_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='typeofsocialnetwork',
            old_name='name_of_country',
            new_name='name_of_socnet',
        ),
        migrations.RemoveField(
            model_name='botinfos',
            name='access_token',
        ),
        migrations.RemoveField(
            model_name='botinfos',
            name='email',
        ),
        migrations.RemoveField(
            model_name='botinfos',
            name='login',
        ),
        migrations.RemoveField(
            model_name='botinfos',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='botinfos',
            name='type_of_social_net',
        ),
        migrations.AddField(
            model_name='botinfosindiffrentsocnet',
            name='access_token',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='dataofoungroupofbots',
            name='group_id',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='monitoringbotonline',
            name='id_bot',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='dataofoungroupofbots',
            name='count_of_friends',
            field=models.CharField(default='', max_length=10),
        ),
    ]