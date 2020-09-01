# Generated by Django 3.1 on 2020-09-01 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0020_auto_20200901_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_order_completion',
            name='status',
            field=models.CharField(blank=True, choices=[('i', 'In progress'), ('h', 'Finish')], default='f', max_length=1),
        ),
    ]
