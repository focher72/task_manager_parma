from django.contrib import admin
from .models import (
    Active_hardware,
    Hardware_adress,
    Hardware_ports,
    Vlan,
    # Hardware_connections,
)
from simple_history.admin import SimpleHistoryAdmin


class Active_hardware_Admin(admin.ModelAdmin):
    list_display = ('name_hardware', 'serial_num', 'ip_adress', 'adress', 'revision',)
    search_fields = ('name_hardware', 'serial_num', 'ip_adress')


class Hardware_ports_Admin(admin.ModelAdmin):
    list_display = ('hardware', 'port_number', 'client_service',)
    list_display_links = ('hardware', 'client_service',)
    readonly_fields = ('create_user', 'create_date')
    list_filter = ('port_vlan', 'hardware',)
    search_fields = ('hardware',)


class Vlan_Admin(admin.ModelAdmin):
    list_display = ('vlan_number', 'vlan_name', 'comment',)
    search_fields = ('vlan_name',)


class Adress_Admin(admin.ModelAdmin):
    list_display = ('adress', 'comment',)
    search_fields = ('adress', 'comment',)


"""
class Hardware_connections_Admin(admin.ModelAdmin):
    list_display = ('hardware_A', 'port_number_A', 'hardware_B', 'port_number_B',)
    list_display_links = ('hardware_A', 'hardware_B',)
"""

admin.site.register(Active_hardware, Active_hardware_Admin)
admin.site.register(Hardware_adress, Adress_Admin)
admin.site.register(Hardware_ports, Hardware_ports_Admin)
admin.site.register(Vlan, Vlan_Admin)
# admin.site.register(Hardware_connections, Hardware_connections_Admin)
