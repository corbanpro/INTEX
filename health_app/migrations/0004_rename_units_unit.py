# Generated by Django 4.1.2 on 2022-11-28 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0003_comorbidity_recipe_remove_meal_calories_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='units',
            new_name='unit',
        ),
    ]
