# Generated by Django 3.2.3 on 2021-05-31 01:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20210530_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 1, 18, 24, 58316, tzinfo=utc)),
        ),
    ]
