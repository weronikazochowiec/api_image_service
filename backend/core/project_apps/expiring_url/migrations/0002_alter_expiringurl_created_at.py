# Generated by Django 3.2.3 on 2021-06-02 14:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ("expiring_url", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expiringurl",
            name="created_at",
            field=models.DateTimeField(
                default=datetime.datetime(2021, 6, 2, 14, 1, 53, 368368, tzinfo=utc)
            ),
        ),
    ]
