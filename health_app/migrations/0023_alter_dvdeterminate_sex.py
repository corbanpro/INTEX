# Generated by Django 4.1.2 on 2022-11-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0022_alter_dvdeterminate_sex'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dvdeterminate',
            name='sex',
            field=models.CharField(default='M', max_length=10),
        ),
    ]
