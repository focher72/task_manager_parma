from django.contrib import admin
from .models import (
    Active_hardware,
    Hardware_adress_history,
    Hardware_adress,
    Change_reason,
    Hardware_ports,
    Vlan,
    Hardware_connections,
)


class Active_hardware_Admin(admin.ModelAdmin):
    # Последовательость имен полей которые надо выводить
    list_display = ('name_hardware', 'serial_num', 'invt_num', 'ip_adress', 'ports',)
    readonly_fields = ('create_user', 'create_date')
    list_filter = ('ports',)
    search_fields = ('name_hardware', 'serial_num', 'invt_num',)


class Hardware_adress_history_Admin(admin.ModelAdmin):
    # Последовательость имен полей которые надо выводить
    list_display = ('hardware', 'adress', 'create_date', 'create_user',)
    list_display_links = ('hardware', 'adress',)
    readonly_fields = ('create_user', 'create_date')
    list_filter = ('hardware',)
    search_fields = ('hardware',)


class Hardware_ports_Admin(admin.ModelAdmin):
    list_display = ('hardware', 'port_number', 'client_service',)
    list_display_links = ('hardware', 'client_service',)
    readonly_fields = ('create_user', 'create_date')
    list_filter = ('port_vlan', 'hardware',)
    search_fields = ('hardware',)


class Vlan_Admin(admin.ModelAdmin):
    list_display = ('vlan_name', 'comment',)
    search_fields = ('vlan_name',)


class Hardware_connections_Admin(admin.ModelAdmin):
    list_display = ('hardware_A', 'port_number_A', 'hardware_B', 'port_number_B',)
    list_display_links = ('hardware_A', 'hardware_B',)


admin.site.register(Active_hardware, Active_hardware_Admin)
admin.site.register(Hardware_adress_history, Hardware_adress_history_Admin)
admin.site.register(Change_reason)
admin.site.register(Hardware_adress)
admin.site.register(Hardware_ports, Hardware_ports_Admin)
admin.site.register(Vlan, Vlan_Admin)
admin.site.register(Hardware_connections, Hardware_connections_Admin)
