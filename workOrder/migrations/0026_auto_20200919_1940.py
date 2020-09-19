# Generated by Django 3.1 on 2020-09-19 12:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0009_auto_20200919_1926'),
        ('workOrder', '0025_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='department',
        ),
        migrations.AlterField(
            model_name='work_order',
            name='dest_section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utility.section'),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
    ]
