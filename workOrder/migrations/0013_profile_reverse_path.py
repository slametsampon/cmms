# Generated by Django 3.1 on 2020-08-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0012_auto_20200826_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='reverse_path',
            field=models.CharField(max_length=3, null=True),
        ),
    ]