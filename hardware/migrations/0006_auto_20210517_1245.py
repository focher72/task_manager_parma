# Generated by Django 3.1.7 on 2021-05-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardware', '0005_auto_20210517_1241'),
    ]

    operations = [
        migrations.AddField(
            model_name='hardware_ports',
            name='port_vlan',
            field=models.ManyToManyField(blank=True, to='hardware.Vlan'),
        ),
        migrations.DeleteModel(
            name='Vlan_ports',
        ),
    ]
