from django.contrib import admin
from .models import Client_lists, Client_shpd_info


class Client_lists_Admin(admin.ModelAdmin):
    # Последовательость имен полей которые надо выводить
    list_display = ('account', 'clnt_type', 'clnt_name', 'abonent_adr',)
    # Имена полей которые нужны как гиперссылки
    list_display_links = ('account',)
    # Поля по которым нужна фильтрация возможно в третей версии его нет
    search_fields = ('account',)
    list_filter = ('clnt_type',)


class Client_shpd_info_Admin(admin.ModelAdmin):
    # Последовательость имен полей которые надо выводить
    list_display = ('account', 'service', 'ip_adr', 'user_name', 'user_pass',)
    # Имена полей которые нужны как гиперссылки
    list_display_links = ('account',)
    # Поля по которым нужна фильтрация возможно в третей версии его нет
    search_fields = ('account__clnt_name',)
    list_filter = ('type_shpd', 'tarplan',)


admin.site.register(Client_lists, Client_lists_Admin)
admin.site.register(Client_shpd_info, Client_shpd_info_Admin)
