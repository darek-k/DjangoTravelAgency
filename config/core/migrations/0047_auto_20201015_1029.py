# Generated by Django 3.1.2 on 2020-10-15 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_profile_comment'),
        ('core', '0046_auto_20201014_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trippurchase',
            old_name='price',
            new_name='final_price',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='adults_number',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='kids_number',
        ),
        migrations.RemoveField(
            model_name='trippurchase',
            name='participants_data',
        ),
        migrations.AddField(
            model_name='trippurchase',
            name='adults_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trippurchase',
            name='kids_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='trippurchase',
            name='main_booker',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.profile'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='trippurchase',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='core.trip'),
        ),
    ]
