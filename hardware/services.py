from django.http import JsonResponse
from .models import (
    Hardware_adress_history,
    Active_hardware,
    Hardware_ports,
    Change_reason
)


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
        change_reason=Change_reason.objects.get(pk=1))
    new_adress_B = Hardware_adress_history.objects.create(
        adress=adress_info_A.adress,
        hardware=Active_hardware.objects.get(pk=hardware_B),
        change_reason=Change_reason.objects.get(pk=1))
    return {
        'hardware_A': f'{adress_info_A.adress}' + ' -> ' + f'{new_adress_A.adress}',
        'hardware_B': f'{adress_info_B.adress}' + ' -> ' + f'{new_adress_B.adress}'
    }


def _change_hardware_ports(hardware_A: int, hardware_B: int):
    Hardware_ports.objects \
        .filter(hardware=Active_hardware.objects.get(pk=hardware_A)) \
        .update(hardware=Active_hardware.objects.get(pk=hardware_B))
