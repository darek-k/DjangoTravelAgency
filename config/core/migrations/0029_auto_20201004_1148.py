# Generated by Django 3.1.2 on 2020-10-04 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_auto_20201004_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='wifi',
            field=models.CharField(choices=[('Tak', 'Tak'), ('Nie', 'Nie')], default='No', max_length=10),
        ),
    ]