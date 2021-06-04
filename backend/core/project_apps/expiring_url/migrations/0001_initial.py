# Generated by Django 3.2.3 on 2021-06-02 13:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("images", "0008_auto_20210602_1557"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExpiringUrl",
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
                ("uuid", models.UUIDField(default=uuid.uuid4)),
                ("created_at", models.DateTimeField()),
                ("expires_at", models.DateTimeField()),
                (
                    "image",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="images.image"
                    ),
                ),
            ],
        ),
    ]
