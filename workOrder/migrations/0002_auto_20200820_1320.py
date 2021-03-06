# Generated by Django 3.1 on 2020-08-20 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workOrder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of section(eg. Maintenance)', max_length=50, null=True)),
                ('initial', models.CharField(help_text='Enter initial of section(eg. Mntc)', max_length=5, null=True)),
                ('description', models.CharField(help_text='Enter description of department', max_length=200, null=True)),
                ('role', models.CharField(blank=True, choices=[('e', 'Executor'), ('o', 'Originator'), ('a', 'Any')], default='o', help_text='Select role', max_length=1)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter name of section(eg. Electrical & Instrumentation)', max_length=50, null=True)),
                ('initial', models.CharField(help_text='Enter initial of section(eg. Elins)', max_length=5, null=True)),
                ('description', models.CharField(help_text='Enter description of section', max_length=200, null=True)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workOrder.department')),
            ],
            options={
                'ordering': ['department', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Work_order_completion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.TextField(help_text='Enter action', max_length=1000, null=True)),
                ('manPower', models.CharField(help_text='Man power name', max_length=100, null=True)),
                ('material', models.TextField(help_text='Enter material', max_length=1000, null=True)),
                ('tool', models.TextField(help_text='Enter action', max_length=1000, null=True)),
                ('date', models.DateField(null=True)),
                ('duration', models.IntegerField(help_text='Enter duration (hours)', null=True)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Work_order_journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prev_user', models.CharField(max_length=3, null=True)),
                ('next_user', models.CharField(max_length=3, null=True)),
                ('comment', models.CharField(help_text='Enter comment', max_length=200, null=True)),
                ('date', models.DateField()),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
        migrations.AddField(
            model_name='profile',
            name='approver',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='initial',
            field=models.CharField(max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='nik',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Work_order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wo_number', models.CharField(help_text='Enter tagnumber(Prodxxxx)', max_length=20, null=True)),
                ('tagnumber', models.CharField(help_text='Enter tagnumber(eg. FT-1405)', max_length=50, null=True)),
                ('problem', models.TextField(help_text='Enter problem', max_length=1000, null=True)),
                ('priority', models.CharField(blank=True, choices=[('n', 'Normal'), ('e', 'Emergency'), ('s', 'Shutdown'), ('o', 'Other')], default='n', help_text='Select priority', max_length=1)),
                ('date_open', models.DateField()),
                ('status', models.CharField(blank=True, max_length=20)),
                ('dest_section', models.ForeignKey(help_text='Select destination section', null=True, on_delete=django.db.models.deletion.SET_NULL, to='workOrder.section')),
                ('originator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['originator', 'status', 'wo_number'],
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='workOrder.section'),
        ),
    ]
