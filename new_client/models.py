from django.db import models
from datetime import datetime
from django_currentuser.db.models import CurrentUserField


class New_client(models.Model):
    fio = models.CharField('ФИО клиента', max_length=250)
    contact = models.TextField('Контактные данные')
    comment = models.CharField('Комментарий', null=True, blank=True,
                               max_length=250)
    adress = models.ForeignKey(
        'Client_adress',
        on_delete=models.CASCADE,
        null=True,
        verbose_name='Адрес',
        related_name='client_adress')
    create_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        # editable=False,
        verbose_name='Дата добавления')
    create_user = CurrentUserField()

    class Meta:
        verbose_name_plural = 'Заявки на подключение'
        verbose_name = 'Заявки на подключение'

    def __str__(self):
        return f'{self.fio}'


class Client_adress(models.Model):
    street = models.CharField('Улица', max_length=100)
    house = models.CharField('Дом', max_length=15)

    class Meta:
        verbose_name_plural = 'Адреса заявок'
        verbose_name = 'Адрес заявки'

    def __str__(self):
        return f'{self.street}' + ' ' + f'{self.house}'
