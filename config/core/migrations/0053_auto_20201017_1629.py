# Generated by Django 3.1.2 on 2020-10-17 14:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0052_trippurchase_test_char_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trippurchase',
            name='main_booker',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
