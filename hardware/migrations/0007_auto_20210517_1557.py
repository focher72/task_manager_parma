# Generated by Django 3.1.7 on 2021-05-17 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0006_auto_20210517_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardware_connections',
            name='port_number_A',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер порта А'),
        ),
        migrations.AlterField(
            model_name='hardware_connections',
            name='port_number_B',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер порта Б'),
        ),
    ]
