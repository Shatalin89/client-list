# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-09 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clients_name', models.CharField(max_length=50)),
                ('clients_middlename', models.CharField(max_length=50)),
                ('clients_lastname', models.CharField(max_length=50)),
                ('clients_age', models.DateField(null=True)),
                ('clients_telephone', models.CharField(max_length=11)),
                ('clients_comments', models.TextField()),
            ],
            options={
                'db_table': 'clients',
            },
        ),
    ]