from django.db import models
from datetime import datetime
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django_currentuser.db.models import CurrentUserField
from oracle_base.models import Client_shpd_info
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler


class Active_hardware(ChangeloggableMixin, models.Model):
    name_hardware = models.CharField('Название', max_length=100)
    serial_num = models.CharField('Серийный номер', max_length=100)
    invt_num = models.CharField('Инвентарный номер', max_length=100, null=True, blank=True)
    revision = models.CharField('Ревизия', max_length=10, null=True, blank=True)
    description = models.CharField('Описание', max_length=250, null=True,
                                   blank=True)
    ip_adress = models.CharField('IP адрес', max_length=15, null=True, blank=True)
    mac_adress = models.CharField('MAC адрес', max_length=250, null=True, blank=True)
    create_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        editable=False,
        verbose_name='Дата добавления')
    create_user = CurrentUserField()

    class Meta:
        verbose_name_plural = 'Активное оборудование'
        verbose_name = 'Активное оборудование'

    def __str__(self):
        return self.name_hardware + ' IP: ' + self.ip_adress


"""
class Active_hardware(ChangeloggableMixin, models.Model):
    name_hardware = models.CharField('Название', max_length=100)
    serial_num = models.CharField('Серийный номер', max_length=100)
    invt_num = models.CharField('Инвентарный номер', max_length=100)
    description = models.CharField('Описание', max_length=250, null=True,
                                   blank=True)
    create_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        editable=False,
        verbose_name='Дата добавления')
    # create_user = CurrentUserField()
    # ports = models.IntegerField('Количество портов', null=True,
    #                             blank=True)
    ip_adress = models.CharField('IP адрес', max_length=15, null=True, blank=True)
    # login = models.CharField('логин', max_length=32)
    # password = models.CharField('пароль', max_length=32)
    # port_proc = models.CharField('проверка порта', max_length=64, null=True,
    #                              blank=True)
    # status_proc = models.CharField('проверка общая', max_length=64, null=True,
    #                                blank=True)
    mac_adress = models.CharField('MAC адрес', max_length=250)
    power = models.CharField('Потребляемая мощность', max_length=20, null=True,
                             blank=True)

    class Meta:
        verbose_name_plural = 'Активное оборудование'
        verbose_name = 'Активное оборудование'

    def __str__(self):
        return self.name_hardware + ' IP: ' + self.ip_adress
"""


post_save.connect(journal_save_handler, sender=Active_hardware)
post_delete.connect(journal_delete_handler, sender=Active_hardware)


class Hardware_adress(models.Model):
    # spot_adress = models.CharField('Название узла', max_length=250)
    adress = models.CharField('Адрес', max_length=250)
    comment = models.CharField('Комментарий', null=True, blank=True,
                               max_length=250)

    class Meta:
        verbose_name_plural = 'Адреса оборудования'
        verbose_name = 'Адрес оборудования'
        ordering = ['adress']

    def __str__(self):
        return self.adress


"""
class Change_reason(models.Model):
    reason_name = models.CharField('Причина изменения', max_length=50)

    class Meta:
        verbose_name_plural = 'Причины именения адреса'
        verbose_name = 'Причины именения адреса'

    def __str__(self):
        return self.reason_name
"""

"""
class Hardware_adress_history(models.Model):
    hardware = models.ForeignKey(
        'Active_hardware',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Оборудование')
    adress = models.ForeignKey(
        'Hardware_adress',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Адрес')
    comment = models.CharField('Комментарий', null=True, blank=True,
                               max_length=250)
    create_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        editable=False,
        verbose_name='Дата добавления')
    create_user = CurrentUserField()

    class Meta:
        verbose_name_plural = 'История перемещения оборудования'
        verbose_name = 'История перемещения оборудования'
"""


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
        verbose_name='Оборудование')
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


@receiver(post_save, sender=Active_hardware)
def add_first_adress(sender, instance, **kwargs):
    """добавление первого адреса"""
    count_adr_history = Hardware_adress_history.objects.filter(hardware=instance).count()
    if count_adr_history == 0:
        Hardware_adress_history.objects.create(
            adress=Hardware_adress.objects.get(
                spot_adress='(~)Коммунистическая, 30. Склад ПармаТел'),
            hardware=instance,
            comment='Автоматическая запись')
