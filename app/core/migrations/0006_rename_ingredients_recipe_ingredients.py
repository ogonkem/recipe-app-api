# Generated by Django 3.2.15 on 2023-01-11 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_ingredient_recipe_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='Ingredients',
            new_name='ingredients',
        ),
    ]
