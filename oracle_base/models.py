from django.db import models


class Client_lists(models.Model):
    account = models.IntegerField('Лицевой номер', unique=True)
    clnt_type = models.BooleanField('ЮР лицо', default=0)
    vip = models.BooleanField('VIP', default=0)
    clnt_name = models.CharField('Имя клиента', null=True, blank=True, max_length=100)
    inn = models.CharField('ИНН', max_length=20, null=True)
    email = models.CharField('Почта', max_length=30, null=True)
    contact = models.CharField('Контактные данные', max_length=250, null=True)

    class Meta:
        verbose_name_plural = 'Список клиентов'
        verbose_name = 'Списоки клиентов'

    def __str__(self):
        return self.clnt_name


class Client_shpd_info(models.Model):
    account = models.ForeignKey(
        Client_lists,
        to_field='account',
        on_delete=models.CASCADE,
        verbose_name='Лицевой номер')
    service = models.IntegerField('Сервисный номер')
    type_shpd = models.CharField('Тип интернета', max_length=50, null=True)
    abonplat = models.IntegerField('Абонплата', default=0)
    tarplan = models.CharField('Тарифный план', max_length=50, null=True)
    adress = models.TextField('Адрес', null=True)
    ip_adr = models.CharField('ИП адрес', max_length=30, null=True)
    mask = models.CharField('Маска', max_length=30, null=True)
    gateway = models.CharField('Шлюз', max_length=30, null=True)
    user_name = models.CharField('Логин', max_length=50, null=True)
    user_pass = models.CharField('Пароль', max_length=50, null=True)
    bdate = models.CharField('Начало действия', max_length=50, null=True)

    class Meta:
        verbose_name_plural = 'Список услуг интернета'
        verbose_name = 'Список услуг интернета'

    def __str__(self):
        return f'{self.account}' + ' IP:' + f'{self.ip_adr}'
