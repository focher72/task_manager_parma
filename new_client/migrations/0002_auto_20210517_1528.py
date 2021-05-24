# Generated by Django 3.1.7 on 2021-05-17 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_client',
            name='contact',
            field=models.TextField(verbose_name='Контактные данные'),
        ),
        migrations.AlterField(
            model_name='new_client',
            name='fio',
            field=models.CharField(max_length=250, verbose_name='ФИО клиента'),
        ),
        migrations.AlterField(
            model_name='new_client',
            name='house',
            field=models.CharField(max_length=15, verbose_name='Дом'),
        ),
        migrations.AlterField(
            model_name='new_client',
            name='street',
            field=models.CharField(max_length=100, verbose_name='Улица'),
        ),
    ]
