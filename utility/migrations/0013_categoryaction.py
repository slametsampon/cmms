# Generated by Django 3.1 on 2020-09-23 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0012_wo_priority'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Finish', 'Finish'), ('Schedule', 'Schedule'), ('Close', 'Close')], default='Pending', help_text='Select Category', max_length=10)),
                ('actions', models.ManyToManyField(help_text='Select actions', to='utility.Action')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]