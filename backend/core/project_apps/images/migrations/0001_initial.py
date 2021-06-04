# Generated by Django 3.2.3 on 2021-05-30 13:35

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import project_apps.images.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Image",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=125)),
                ("description", models.CharField(max_length=250, null=True)),
                (
                    "image",
                    models.ImageField(
                        upload_to=project_apps.images.models.user_directory_path
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=datetime.datetime(
                            2021, 5, 30, 13, 35, 23, 904911, tzinfo=utc
                        )
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
