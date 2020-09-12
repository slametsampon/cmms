# Generated by Django 3.1 on 2020-09-12 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workOrder', '0023_auto_20200901_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of Status(eg. Open, Close, Reject...)', max_length=20, null=True)),
                ('description', models.CharField(help_text='Enter description of Status', max_length=100, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='work_order',
            name='status_wo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workOrder.status'),
        ),
    ]