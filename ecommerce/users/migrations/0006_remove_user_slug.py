# Generated by Django 4.2 on 2023-04-27 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_address_alter_user_city_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="user", name="slug",),
    ]
