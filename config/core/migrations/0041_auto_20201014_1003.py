# Generated by Django 3.1.2 on 2020-10-14 08:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0040_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 14, 8, 3, 35, 601062, tzinfo=utc)),
        ),
    ]
