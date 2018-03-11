# Generated by Django 2.0.2 on 2018-03-05 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='blog.Category'),
        ),
    ]