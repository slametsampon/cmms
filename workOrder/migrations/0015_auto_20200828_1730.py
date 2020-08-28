# Generated by Django 3.1 on 2020-08-28 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0014_auto_20200826_1406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='work_order_journal',
            options={'ordering': ['-date', '-time']},
        ),
        migrations.AlterField(
            model_name='work_order_completion',
            name='tool',
            field=models.TextField(help_text='Enter action', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='work_order_journal',
            name='action',
            field=models.CharField(blank=True, default='f', max_length=1),
        ),
        migrations.AlterField(
            model_name='work_order_journal',
            name='comment',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
