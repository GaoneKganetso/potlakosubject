# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-01-12 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=7, verbose_name='are you a male or female?')),
            ],
        ),
    ]