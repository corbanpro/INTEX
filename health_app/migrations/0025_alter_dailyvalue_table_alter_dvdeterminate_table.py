# Generated by Django 4.1.2 on 2022-11-30 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('health_app', '0024_alter_dvdeterminate_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dailyvalue',
            table='DailyValues',
        ),
        migrations.AlterModelTable(
            name='dvdeterminate',
            table='DailyValueDeterminates',
        ),
    ]
