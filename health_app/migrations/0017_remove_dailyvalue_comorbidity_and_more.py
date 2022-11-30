# Generated by Django 4.1.2 on 2022-11-30 17:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0016_alter_meal_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyvalue',
            name='comorbidity',
        ),
        migrations.AddField(
            model_name='comorbidity',
            name='daily_value',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='health_app.dailyvalue'),
            preserve_default=False,
        ),
    ]
