# Generated by Django 3.1 on 2020-09-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0009_auto_20200919_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='initial',
            field=models.CharField(help_text='Enter initial of section(eg. Mntc)', max_length=5, null=True),
        ),
    ]
