# Generated by Django 4.1.2 on 2022-11-30 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0019_dailyvalue_water'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comorbidity',
            new_name='DvDeterminate',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='comorbidity',
            new_name='dv_determinate',
        ),
    ]