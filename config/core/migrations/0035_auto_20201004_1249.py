# Generated by Django 3.1.2 on 2020-10-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_auto_20201004_1242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='stars',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, max_length=5),
        ),
    ]
