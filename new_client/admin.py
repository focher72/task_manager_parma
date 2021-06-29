from django.contrib import admin
from .models import New_client, Client_adress


class New_client_Admin(admin.ModelAdmin):
    list_display = ('fio', 'contact', 'create_date', 'adress')
    list_display_links = ('fio', 'adress',)
    readonly_fields = ('create_user', 'create_date')
    list_filter = ('adress', 'create_user',)
    search_fields = ('fio',)


class Client_adress_Admin(admin.ModelAdmin):
    list_display = ('street', 'house',)
    # list_display_links = ('fio', 'adress',)
    # readonly_fields = ('create_user', 'create_date')
    list_filter = ('street', 'house',)
    #  search_fields = ('fio',)


admin.site.register(New_client, New_client_Admin)
admin.site.register(Client_adress, Client_adress_Admin)
