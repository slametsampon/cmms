# Generated by Django 3.1 on 2020-09-20 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0010_department_initial'),
        ('workOrder', '0029_auto_20200920_1445'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work_order',
            name='status_wo',
        ),
        migrations.AlterField(
            model_name='work_order',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utility.action'),
        ),
    ]
