from django.db import models
from datetime import datetime
from django_currentuser.db.models import CurrentUserField
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from oracle_base.models import Client_lists
from changelog.mixins import ChangeloggableMixin
from changelog.signals import journal_save_handler, journal_delete_handler


class Task(ChangeloggableMixin, models.Model):
    """Список всех заявок"""
    TYPE_CATEGORY_ON_MODEL = (
        ('tech', 'Техподдержка'),
        ('abon', 'Абонентский'),
    )
    task_text = models.TextField('Описание')
    client = models.ForeignKey(
        Client_lists,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Клиент')
    source = models.ForeignKey(
        'Task_source',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Источник')
    type = models.ForeignKey(
        'Task_types',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Тип заявки')
    category = models.CharField(
        choices=TYPE_CATEGORY_ON_MODEL,
        max_length=10,
        verbose_name='Категория заявки',
        default='tech',
        null=True)
    create_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        editable=False,
        verbose_name='Дата добавления')
    create_user = CurrentUserField()

    class Meta:
        verbose_name_plural = 'Заявки'
        verbose_name = 'Заявка'
        ordering = ('create_date',)

    def __str__(self):
        return self.task_text[0:20] + ' от: ' f'{self.create_date}'[0:20]


class Status(models.Model):
    """Виды статусов"""
    status_name = models.CharField('Статус', max_length=10)

    class Meta:
        verbose_name_plural = 'Статусы'
        verbose_name = 'Статус'

    def __str__(self):
        return self.status_name


class Task_status(ChangeloggableMixin, models.Model):
    """Список изменений статуса заявок"""
    status = models.ForeignKey(
        'Status',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Статус',
        related_name='statuses')
    task = models.ForeignKey(
        'Task',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Заявка',
        related_name='statuses')
    start_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        verbose_name='Начало действия')
    end_date = models.DateTimeField(
        default=datetime(2999, 12, 31),
        db_index=True,
        verbose_name='Окончание действия')
    comment = models.TextField('Комментарий', null=True)
    create_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        editable=False,
        verbose_name='Дата добавления')
    create_user = CurrentUserField()

    class Meta:
        verbose_name_plural = 'Статусы заявок'
        verbose_name = 'Статус заявки'
        ordering = ('create_date',)

    def __str__(self):
        return f'{self.task}' + ' ' + f'{self.status}'


class Task_types(models.Model):
    """Тип заявки (проблемы с инетом, тв и т.п.)"""
    TYPE_CATEGORY_ON_MODEL = (
        ('tech', 'Техподдержка'),
        ('abon', 'Абонентский'),
    )
    task_name = models.CharField('Тип заявки', max_length=20)
    category = models.CharField(
        choices=TYPE_CATEGORY_ON_MODEL,
        max_length=10,
        default='tech',
        verbose_name='Категория заявки',
        null=True)

    class Meta:
        verbose_name_plural = 'Типы заявок'
        verbose_name = 'Тип заявки'

    def __str__(self):
        return self.task_name


class Task_source(models.Model):
    """Источник получения заявки"""
    source_name = models.CharField('Источник', max_length=100)

    class Meta:
        verbose_name_plural = 'Источники заявок'
        verbose_name = 'Источник заявок'

    def __str__(self):
        return self.source_name


class Task_user_work(ChangeloggableMixin, models.Model):
    """Таблица исполнителей"""
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Исполнитель',
        related_name='task_work')
    task = models.ForeignKey(
        'Task',
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Заявка',
        related_name='task_user')
    start_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        verbose_name='Начало действия')
    comment = models.TextField('Комментарий', null=True)
    end_date = models.DateTimeField(
        default=datetime(2999, 12, 31),
        db_index=True,
        verbose_name='Окончание действия')
    create_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        editable=False,
        verbose_name='Дата добавления')
    create_user = CurrentUserField()

    class Meta:
        verbose_name_plural = 'История исполнителей'
        verbose_name = 'История исполнителя'
        ordering = ('create_date',)

    def __str__(self):
        return f'{self.task}' + ' ' f'{self.user}'


class Task_messages(ChangeloggableMixin, models.Model):
    """ Комментарии сотрудников к заявке """
    task = models.ForeignKey(
        Task,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name='Заявка',
        related_name='task_messages')
    messages_text = models.TextField('Сообщение')
    file = models.FileField(upload_to='documents/%Y/%m/%d/', null=True, blank=True)
    create_date = models.DateTimeField(
        default=datetime.now,
        db_index=True,
        editable=False,
        verbose_name='Дата добавления')
    create_user = CurrentUserField()

    class Meta:
        verbose_name_plural = 'Комментарии к заявкам'
        verbose_name = 'Комментарии к заявке'
        ordering = ('create_date',)

    def __str__(self):
        return self.messages_text


post_save.connect(journal_save_handler, sender=Task)
post_delete.connect(journal_delete_handler, sender=Task)
post_save.connect(journal_save_handler, sender=Task_user_work)
post_delete.connect(journal_delete_handler, sender=Task_user_work)


@receiver(post_save, sender=Task)
def add_first_status_and_user(sender, instance, **kwargs):
    """добавление первого статуса и пользователя"""
    count_status = Task_status.objects.filter(task=instance).count()
    count_user = Task_user_work.objects.filter(task=instance).count()
    if count_status == 0:
        Task_status.objects.create(
            status=Status.objects.get(status_name='Новая'),
            task=instance,
            comment='[AUTO]',
            create_user=instance.create_user)
    if count_user == 0:
        Task_user_work.objects.create(
            user=User.objects.get(username='Без_исполнителя'),
            task=instance,
            comment='[AUTO]',
            create_user=instance.create_user)


@receiver(pre_save, sender=Task_status)
def update_last_status(sender, instance, **kwargs):
    """Изменение даты предыдущего статуса на текущее время"""
    Task_status.objects.filter(
        task=instance.task,
        end_date__gte=instance.start_date
    ).update(end_date=instance.start_date)


@receiver(pre_save, sender=Task_user_work)
def update_last_user_work(sender, instance, **kwargs):
    """Изменение даты предыдущего пользователя на текущее время"""
    Task_user_work.objects.filter(
        task=instance.task,
        end_date__gte=instance.start_date
    ).update(end_date=instance.start_date)


@receiver(post_save, sender=Task_user_work)
def change_status(sender, instance, **kwargs):
    """добавление статуса новой заявки в таблицу со статусами"""
    if instance.user.username != 'Без_исполнителя':
        current_status = Task_status.objects.get(
            task=instance.task,
            end_date__gte=datetime.now()
        )
        if current_status.status.status_name != 'В работе':
            Task_status.objects.create(
                status=Status.objects.get(status_name='В работе'),
                task=instance.task,
                comment='[AUTO]',
                create_user=instance.create_user
            )
