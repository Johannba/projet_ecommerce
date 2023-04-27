# Generated by Django 4.2 on 2023-04-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_alter_user_address_alter_user_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="civility",
            field=models.CharField(
                choices=[("Masculin", "Masculin"), ("Féminin", "Féminin")],
                default="",
                max_length=8,
            ),
            preserve_default=False,
        ),
    ]
