from .models import (
    Hardware_adress_history,
    Active_hardware,
    Hardware_ports
)
from rest_framework import filters


class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])


def _get_hardware_adress_info(hardware: int):
    """ получение информации о текущем расположении оборудования """
    hardware_adr_info = Hardware_adress_history.objects \
        .filter(hardware=hardware) \
        .latest('create_date')
    return hardware_adr_info


def _change_hardware_adress(hardware_A: int, hardware_B: int):
    """ Меняет адрес оборудования с другим оборудованием """
    adress_info_A = _get_hardware_adress_info(hardware_A)
    adress_info_B = _get_hardware_adress_info(hardware_B)
    new_adress_A = Hardware_adress_history.objects.create(
        adress=adress_info_B.adress,
        hardware=Active_hardware.objects.get(pk=hardware_A),
        comment='[AUTO] Замена оборудования местаими')
    new_adress_B = Hardware_adress_history.objects.create(
        adress=adress_info_A.adress,
        hardware=Active_hardware.objects.get(pk=hardware_B),
        comment='[AUTO] Замена оборудования местаими')
    return {
        'hardware_A': f'{adress_info_A.adress}' + ' -> ' + f'{new_adress_A.adress}',
        'hardware_B': f'{adress_info_B.adress}' + ' -> ' + f'{new_adress_B.adress}'
    }


def _change_hardware_ports(hardware_A: int, hardware_B: int):
    Hardware_ports.objects \
        .filter(hardware=Active_hardware.objects.get(pk=hardware_A)) \
        .update(hardware=Active_hardware.objects.get(name_hardware='!Для перемещения'))
    Hardware_ports.objects \
        .filter(hardware=Active_hardware.objects.get(pk=hardware_B)) \
        .update(hardware=Active_hardware.objects.get(pk=hardware_A))
    Hardware_ports.objects \
        .filter(hardware=Active_hardware.objects.get(name_hardware='!Для перемещения')) \
        .update(hardware=Active_hardware.objects.get(pk=hardware_B))
