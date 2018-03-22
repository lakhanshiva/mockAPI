# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-22 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]