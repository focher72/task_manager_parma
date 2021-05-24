from hardware import models, serializers
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from .services import _change_hardware_adress, _change_hardware_ports


def change_hardware(request):
    hardware_A = request.GET.get('hardware_A')
    hardware_B = request.GET.get('hardware_B')
    try:
        result = _change_hardware_adress(hardware_A=hardware_A, hardware_B=hardware_B)
        _change_hardware_ports(hardware_A=hardware_A, hardware_B=hardware_B)
        return JsonResponse({'change': True, 'adress': result})
    except models.Hardware_adress_history.DoesNotExist:
        return JsonResponse({'change': False,
                             'problem': 'hardware not found'})


class ActiveHardwareViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Active_hardware.objects.all()
    serializer_class = serializers.ActiveHardwareSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['create_user']
    search_fields = ['name_hardware', 'serial_num', 'invt_num']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
