# Generated by Django 3.2.3 on 2021-05-31 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plans', '0002_rename_thumbnail_sizes_plan_available_thumbnail_sizes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='ability_to_generate_expiring_links',
            new_name='can_generate_expiring_links',
        ),
        migrations.RenameField(
            model_name='plan',
            old_name='presence_a_link_to_org_img',
            new_name='has_access_to_org_img',
        ),
    ]
