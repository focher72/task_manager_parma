from django.db import models
from datetime import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_currentuser.db.models import CurrentUserField
from oracle_base.models import Client_shpd_info
from simple_history.models import HistoricalRecords


class Active_hardware(models.Model):
    """ Таблица основная с оборудованием """
    name_hardware = models.CharField('Название', max_length=100)
    serial_num = models.CharField('Серийный номер', max_length=100)
    invt_num = models.CharField('Инвентарный номер', max_length=100, null=True, blank=True)
    adress = models.ForeignKey(
        'Hardware_adress',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Адрес')
    revision = models.CharField('Ревизия', max_length=10, null=True, blank=True)
    description = models.CharField('Описание', max_length=250, null=True,
                                   blank=True)
    ip_adress = models.CharField('IP адрес', max_length=15, null=True, blank=True)
    mac_adress = models.CharField('MAC адрес', max_length=250, null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = 'Активное оборудование'
        verbose_name = 'Активное оборудование'

    def __str__(self):
        return self.name_hardware


class Active_hardware_history(models.Model):
    """ Не управляемая таблица с историей оборудования """
    id = models.IntegerField()
    name_hardware = models.CharField('Название', max_length=100)
    serial_num = models.CharField('Серийный номер', max_length=100)
    invt_num = models.CharField('Инвентарный номер', max_length=100, null=True, blank=True)
    adress = models.ForeignKey(
        'Hardware_adress',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Адрес')
    revision = models.CharField('Ревизия', max_length=10, null=True, blank=True)
    description = models.CharField('Описание', max_length=250, null=True,
                                   blank=True)
    ip_adress = models.CharField('IP адрес', max_length=15, null=True, blank=True)
    mac_adress = models.CharField('MAC адрес', max_length=250, null=True, blank=True)
    history_id = models.IntegerField(primary_key=True)
    history_change_reason = models.TextField('Причина изменения')
    history_date = models.DateTimeField('Дата изменения')
    history_type = models.CharField('Тип изменения', max_length=1, null=True, blank=True)
    history_user = CurrentUserField()

    class Meta:
        managed = False
        db_table = 'hardware_historicalactive_hardware'

    def __str__(self):
        return self.name_hardware


class Hardware_adress(models.Model):
    """ Адреса оборудования или узлы """
    adress = models.CharField('Адрес', max_length=250)
    comment = models.CharField('Комментарий', null=True, blank=True,
                               max_length=250)

    class Meta:
        verbose_name_plural = 'Адреса оборудования'
        verbose_name = 'Адрес оборудования'
        ordering = ['adress']

    def __str__(self):
        return self.adress


class Vlan(models.Model):
    vlan_number = models.IntegerField('Номер VLAN')
    vlan_name = models.CharField('Название', max_length=50, unique=True)
    comment = models.CharField('Комментарий', null=True, blank=True,
                               max_length=250)

    class Meta:
        verbose_name_plural = 'VLAN'
        verbose_name = 'VLAN'

    def __str__(self):
        return self.vlan_name


class Hardware_ports(models.Model):
    hardware = models.ForeignKey(
        'Active_hardware',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Оборудование',
        related_name="hardware_ports")
    port_number = models.IntegerField('Номер порта')
    client_service = models.ForeignKey(
        Client_shpd_info,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Услуга клиента')
    port_vlan = models.ManyToManyField(Vlan, blank=True, related_name="vlan_ports")
    comment = models.CharField('Комментарий', null=True, blank=True,
                               max_length=250)
    create_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        editable=False,
        verbose_name='Дата добавления')
    create_user = CurrentUserField()

    class Meta:
        verbose_name_plural = 'Занятые порты'
        verbose_name = 'Занятые порты'

    def __str__(self):
        return f'{self.hardware__name_hardware}' + '№ ' + f'{self.port_number}'


"""
class Hardware_connections(models.Model):
    hardware_A = models.ForeignKey(
        'Active_hardware',
        on_delete=models.CASCADE,
        related_name='hardware_A',
        verbose_name='Оборудование А')
    port_number_A = models.IntegerField('Номер порта А', null=True, blank=True)
    hardware_B = models.ForeignKey(
        'Active_hardware',
        on_delete=models.CASCADE,
        related_name='hardware_B',
        verbose_name='Оборудование Б')
    port_number_B = models.IntegerField('Номер порта Б', null=True, blank=True)
    comment = models.CharField('Комментарий', null=True, blank=True,
                               max_length=250)
    create_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        editable=False,
        verbose_name='Дата добавления')
    create_user = CurrentUserField()

    class Meta:
        verbose_name_plural = 'Соединения коммутаторов'
        verbose_name = 'Соединения коммутаторов'
"""
