# Generated by Django 3.1 on 2020-09-21 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0035_auto_20200921_1127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wo_instruction',
            old_name='action',
            new_name='instruction',
        ),
        migrations.AddField(
            model_name='wo_instruction',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='wo_instruction',
            name='time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='wo_journal',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='wo_journal',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]