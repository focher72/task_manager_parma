# Generated by Django 3.1.7 on 2021-05-17 15:57

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_currentuser.db.models.fields
import django_currentuser.middleware


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('task_manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(choices=[('tech', 'Техподдержка'), ('abon', 'Абонентский')], max_length=10, null=True, verbose_name='Категория заявки'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime.now, editable=False, verbose_name='Дата добавления'),
        ),
        migrations.AlterField(
            model_name='task',
            name='create_user',
            field=django_currentuser.db.models.fields.CurrentUserField(default=django_currentuser.middleware.get_current_authenticated_user, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
