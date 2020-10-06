# Generated by Django 3.1.2 on 2020-10-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_auto_20201004_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='air_condition',
            field=models.CharField(choices=[('Tak', 'Tak'), ('Nie', 'Nie')], default='Nie', max_length=10),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='gym',
            field=models.CharField(choices=[('Tak', 'Tak'), ('Nie', 'Nie')], default='Nie', max_length=10),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='restaurant',
            field=models.CharField(choices=[('Tak', 'Tak'), ('Nie', 'Nie')], default='Nie', max_length=10),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='room_service',
            field=models.CharField(choices=[('Tak', 'Tak'), ('Nie', 'Nie')], default='Nie', max_length=10),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='stars',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), (3, 3), ('4', 4), ('5', '5')], default=1, max_length=5),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='swimming_pool',
            field=models.CharField(choices=[('Tak', 'Tak'), ('Nie', 'Nie')], default='Nie', max_length=10),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='wifi',
            field=models.CharField(choices=[('Tak', 'Tak'), ('Nie', 'Nie')], default='Nie', max_length=10),
        ),
    ]