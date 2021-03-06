# Generated by Django 3.1 on 2020-08-26 07:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0013_profile_reverse_path'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work_order_journal',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='work_order_journal',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
