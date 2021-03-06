# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-30 07:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientlist', '0004_placeinfo_place_flag_set_sceme'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceSector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sector_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'place_sector',
            },
        ),
        migrations.AddField(
            model_name='placeinfo',
            name='place_current_count',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='placescheme',
            name='place_sector',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clientlist.PlaceSector'),
        ),
    ]
