# Generated by Django 3.1.7 on 2021-07-02 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oracle_base', '0002_client_lists_vip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client_lists',
            name='abonent_adr',
        ),
        migrations.AddField(
            model_name='client_shpd_info',
            name='abonent_adr',
            field=models.TextField(null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='client_shpd_info',
            name='abonplat',
            field=models.IntegerField(default=0, verbose_name='Абонплата'),
        ),
        migrations.AddField(
            model_name='client_shpd_info',
            name='gateway',
            field=models.CharField(max_length=30, null=True, verbose_name='Шлюз'),
        ),
        migrations.AddField(
            model_name='client_shpd_info',
            name='mask',
            field=models.CharField(max_length=30, null=True, verbose_name='Маска'),
        ),
        migrations.AlterField(
            model_name='client_lists',
            name='clnt_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя клиента'),
        ),
        migrations.AlterField(
            model_name='client_lists',
            name='email',
            field=models.CharField(max_length=30, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='client_shpd_info',
            name='ip_adr',
            field=models.CharField(max_length=30, null=True, verbose_name='ИП адрес'),
        ),
    ]