from django_filters import rest_framework as filters
from . import models


class PortsFilter(filters.FilterSet):
    class Meta:
        model = models.Hardware_ports
        fields = {
            'hardware': ['exact'],
        }


class HardwareAdressFilter(filters.FilterSet):
    class Meta:
        model = models.Hardware_adress
        fields = {
            'adress': ['icontains', 'exact'],
            'comment': ['icontains', 'exact'],
        }


class ActiveHardwareFilter(filters.FilterSet):
    class Meta:
        model = models.Active_hardware
        fields = {
            'ip_adress': ['icontains', 'exact'],
            'name_hardware': ['icontains', 'exact'],
            'serial_num': ['icontains', 'exact'],
            'adress__adress': ['icontains', 'exact'],
        }


class ActiveHardwareHistoryFilter(filters.FilterSet):
    class Meta:
        model = models.Active_hardware_history
        fields = {
            'id': ['exact'],
            'ip_adress': ['icontains', 'exact'],
            'name_hardware': ['icontains', 'exact'],
            'serial_num': ['icontains', 'exact'],
            'adress__adress': ['icontains', 'exact'],
        }


class VlanFilter(filters.FilterSet):
    class Meta:
        model = models.Vlan
        fields = {
            'vlan_number': ['exact'],
            'vlan_name': ['icontains', 'exact'],
            'comment': ['icontains', 'exact'],
        }
