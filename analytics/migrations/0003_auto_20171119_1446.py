# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-19 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("analytics", "0002_auto_20171119_1413")]

    operations = [
        migrations.AlterField(
            model_name="pageview", name="timestamp", field=models.DateTimeField()
        )
    ]
