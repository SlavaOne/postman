# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netoko', '0006_monitoringbotonline_monitoringbotonlinedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Botinfosindiffrentsocnet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_phone', models.CharField(default='', max_length=200)),
                ('login', models.CharField(default='', max_length=200)),
                ('describe', models.TextField()),
                ('bot_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netoko.Botinfos')),
                ('type_of_social_net', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='netoko.Typeofsocialnetwork')),
            ],
        ),
        migrations.AddField(
            model_name='dataofbots',
            name='type_of_social_net',
            field=models.CharField(default='', max_length=20),
        ),
    ]