from django.db import models
from datetime import datetime
from django_currentuser.db.models import CurrentUserField


class New_client(models.Model):
    fio = models.CharField('ФИО клиента', max_length=250)
    contact = models.TextField('Контактные данные')
    street = models.CharField('Улица', max_length=100)
    house = models.CharField('Дом', max_length=15)
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
        return self.fio + ' ' + self.street + ' ' + self.house
