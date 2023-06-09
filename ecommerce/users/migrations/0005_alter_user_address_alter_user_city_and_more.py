# Generated by Django 4.2 on 2023-04-27 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("addresses", "0001_initial"),
        ("users", "0004_rename_k_bis_user_k_bis"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="address",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="address",
                to="addresses.address",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="city",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="country",
                to="addresses.country",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="civility",
            field=models.CharField(
                blank=True,
                choices=[("Masculin", "Masculin"), ("Féminin", "Féminin")],
                max_length=8,
            ),
        ),
    ]
