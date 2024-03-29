# Generated by Django 3.1.7 on 2021-05-14 15:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('oracle_base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Active_hardware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_hardware', models.CharField(max_length=100, verbose_name='Название')),
                ('serial_num', models.CharField(max_length=100, verbose_name='Серийный номер')),
                ('invt_num', models.CharField(max_length=100, verbose_name='Инвентарный номер')),
                ('description', models.CharField(blank=True, max_length=250, null=True, verbose_name='Описание')),
                ('create_date', models.DateTimeField(db_index=True, default=datetime.datetime.now, editable=False, verbose_name='Дата добавления')),
                ('ports', models.IntegerField(blank=True, null=True, verbose_name='Количество портов')),
                ('ip_adress', models.CharField(max_length=15, verbose_name='IP адрес')),
                ('login', models.CharField(max_length=32, verbose_name='логин')),
                ('password', models.CharField(max_length=32, verbose_name='пароль')),
                ('port_proc', models.CharField(blank=True, max_length=64, null=True, verbose_name='проверка порта')),
                ('status_proc', models.CharField(blank=True, max_length=64, null=True, verbose_name='проверка общая')),
                ('mac_adress', models.CharField(max_length=250, verbose_name='MAC адрес')),
                ('power', models.CharField(blank=True, max_length=20, null=True, verbose_name='Потребляемая мощность')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Активное оборудование',
                'verbose_name_plural': 'Активное оборудование',
            },
        ),
        migrations.CreateModel(
            name='Change_reason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason_name', models.CharField(max_length=50, verbose_name='Причина изменения')),
            ],
            options={
                'verbose_name': 'Причины именения адреса',
                'verbose_name_plural': 'Причины именения адреса',
            },
        ),
        migrations.CreateModel(
            name='Hardware_adress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spot_adress', models.CharField(max_length=250, verbose_name='Название узла')),
                ('adress', models.CharField(max_length=250, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Адрес оборудования',
                'verbose_name_plural': 'Адреса оборудования',
            },
        ),
        migrations.CreateModel(
            name='Hardware_ports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port_number', models.IntegerField(verbose_name='Номер порта')),
                ('comment', models.CharField(blank=True, max_length=250, null=True, verbose_name='Комментарий')),
                ('create_date', models.DateTimeField(db_index=True, default=datetime.datetime.now, editable=False, verbose_name='Дата добавления')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='oracle_base.client_lists', verbose_name='Клиент')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hardware', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hardware.active_hardware', verbose_name='Оборудование')),
            ],
            options={
                'verbose_name': 'Занятые порты',
                'verbose_name_plural': 'Занятые порты',
            },
        ),
        migrations.CreateModel(
            name='Hardware_adress_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=250, null=True, verbose_name='Комментарий')),
                ('create_date', models.DateTimeField(db_index=True, default=datetime.datetime.now, editable=False, verbose_name='Дата добавления')),
                ('adress', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hardware.hardware_adress', verbose_name='Адрес')),
                ('change_reason', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hardware.change_reason', verbose_name='Причина изменения')),
                ('create_user', django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('hardware', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hardware.active_hardware', verbose_name='Оборудование')),
            ],
            options={
                'verbose_name': 'История перемещения оборудования',
                'verbose_name_plural': 'История перемещения оборудования',
            },
        ),
    ]
