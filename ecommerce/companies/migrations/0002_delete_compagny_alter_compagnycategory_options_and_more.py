# Generated by Django 4.2 on 2023-04-10 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_options_remove_user_company_user_compagny_and_more"),
        ("companies", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="compagny",),
        migrations.AlterModelOptions(
            name="compagnycategory",
            options={
                "ordering": ["name"],
                "verbose_name": "compagnycategory",
                "verbose_name_plural": "compagnycategories",
            },
        ),
        migrations.AlterField(
            model_name="compagnycategory",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
