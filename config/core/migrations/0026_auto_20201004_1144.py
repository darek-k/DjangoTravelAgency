# Generated by Django 3.1.2 on 2020-10-04 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_auto_20201004_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='swimming_pool',
            field=models.CharField(choices=[(True, 'Yes'), (False, 'No')], default=False, max_length=10),
        ),
    ]
