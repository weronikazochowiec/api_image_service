# Generated by Django 3.2.3 on 2021-05-30 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_rename_thumbnail_sizes_plan_available_thumbnail_sizes'),
        ('users', '0002_alter_customuser_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='plans.plan'),
        ),
    ]