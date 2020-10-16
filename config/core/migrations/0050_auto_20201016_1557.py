# Generated by Django 3.1.2 on 2020-10-16 13:57

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_country_country_image2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='country_image2',
        ),
        migrations.AlterField(
            model_name='country',
            name='country_image',
            field=models.ImageField(null=True, upload_to=core.models.get_country_image_path),
        ),
    ]
