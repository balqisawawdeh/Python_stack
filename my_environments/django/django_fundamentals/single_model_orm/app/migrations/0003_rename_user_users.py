# Generated by Django 5.0.3 on 2024-03-28 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_users_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='users',
        ),
    ]