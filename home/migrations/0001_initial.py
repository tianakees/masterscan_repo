# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-08 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('email', models.CharField(max_length=200, verbose_name='Email-ID')),
                ('subject', models.CharField(max_length=200, verbose_name='Subject')),
                ('message', models.CharField(max_length=10000, verbose_name='Message')),
            ],
            options={
                'verbose_name_plural': 'Submissions',
                'verbose_name': 'Submissions',
            },
        ),
    ]