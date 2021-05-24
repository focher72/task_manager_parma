from django.contrib import admin
from .models import New_client


class New_client_Admin(admin.ModelAdmin):
    # Последовательость имен полей которые надо выводить
    list_display = ('fio', 'contact', 'street', 'house', 'create_date',)
    # Имена полей которые нужны как гиперссылки
    # list_display_links = ('account',)
    # Поля по которым нужна фильтрация возможно в третей версии его нет
    search_fields = ('fio',)
    readonly_fields = ('create_user', 'create_date')
    list_filter = ('street',)


admin.site.register(New_client, New_client_Admin)
