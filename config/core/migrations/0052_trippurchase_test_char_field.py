# Generated by Django 3.1.2 on 2020-10-17 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0051_auto_20201017_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='trippurchase',
            name='test_char_field',
            field=models.CharField(default='', max_length=50),
        ),
    ]
