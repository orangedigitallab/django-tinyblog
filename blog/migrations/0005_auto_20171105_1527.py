# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 15:27
from __future__ import unicode_literals

import blog.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blog", "0004_image")]

    operations = [
        migrations.AlterField(
            model_name="image",
            name="photo",
            field=models.ImageField(
                upload_to=blog.utils.FileUploader(path="entry/images")
            ),
        )
    ]
