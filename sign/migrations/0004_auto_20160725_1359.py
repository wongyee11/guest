# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-25 05:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0003_auto_20160725_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('limit', models.IntegerField()),
                ('status', models.BooleanField()),
                ('address', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(verbose_name='date events')),
                ('create_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='guest',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='events',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sign.Event'),
        ),
        migrations.DeleteModel(
            name='Events',
        ),
    ]