# Generated by Django 3.1 on 2020-08-23 22:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workOrder', '0007_auto_20200824_0514'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_order_completion',
            name='acted_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
