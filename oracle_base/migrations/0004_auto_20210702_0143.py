# Generated by Django 3.1.7 on 2021-07-02 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oracle_base', '0003_auto_20210702_0141'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client_shpd_info',
            old_name='abonent_adr',
            new_name='adress',
        ),
    ]
