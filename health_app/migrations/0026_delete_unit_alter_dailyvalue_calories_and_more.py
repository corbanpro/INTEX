# Generated by Django 4.1.2 on 2022-12-01 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0025_alter_dailyvalue_table_alter_dvdeterminate_table'),
    ]

    operations = [
        migrations.DeleteModel(
            name='unit',
        ),
        migrations.AlterField(
            model_name='dailyvalue',
            name='calories',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dailyvalue',
            name='carbs',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dailyvalue',
            name='fat',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dailyvalue',
            name='phosphorus',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dailyvalue',
            name='potassium',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dailyvalue',
            name='protein',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dailyvalue',
            name='sodium',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='calories',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='carbs',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='fat',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='phosphorus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='potassium',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='protein',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='sodium',
            field=models.IntegerField(default=0),
        ),
    ]