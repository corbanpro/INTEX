# Generated by Django 4.1.2 on 2022-11-30 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0018_dailyvalue_description_alter_comorbidity_daily_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyvalue',
            name='water',
            field=models.FloatField(default=20),
        ),
    ]