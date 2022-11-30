# Generated by Django 4.1.2 on 2022-11-30 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0017_remove_dailyvalue_comorbidity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyvalue',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comorbidity',
            name='daily_value',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='health_app.dailyvalue'),
        ),
    ]