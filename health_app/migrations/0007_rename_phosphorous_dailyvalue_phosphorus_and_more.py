# Generated by Django 4.1.2 on 2022-11-29 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0006_alter_user_birthdate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dailyvalue',
            old_name='phosphorous',
            new_name='phosphorus',
        ),
        migrations.RemoveField(
            model_name='dailyvalue',
            name='water',
        ),
    ]
