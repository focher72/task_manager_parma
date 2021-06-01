from hardware import models, serializers
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
from .services import _change_hardware_adress, _change_hardware_ports, \
                      DynamicSearchFilter


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
        DynamicSearchFilter,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['create_user']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdressViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Hardware_adress.objects.all()
    serializer_class = serializers.HardwareAdressSerializer
    filter_backends = (
        DjangoFilterBackend,
        DynamicSearchFilter
    )
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ChangeReasonViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Change_reason.objects.all()
    serializer_class = serializers.ChangeReasonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HardwareAdressViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Hardware_adress_history.objects.all()
    serializer_class = serializers.HardwareAdressHistorySerializer
    filter_backends = (
        DjangoFilterBackend,
        DynamicSearchFilter,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['create_user']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VlanViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Vlan.objects.all()
    serializer_class = serializers.VlanSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VlanReadViewSet(viewsets.ReadOnlyModelViewSet):
    """Все заявки"""
    queryset = models.Vlan.objects.all()
    serializer_class = serializers.VlanReadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HardwarePortsViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Hardware_ports.objects.all()
    serializer_class = serializers.HardwarePortsSerializer
    filter_backends = (
        DjangoFilterBackend,
        DynamicSearchFilter,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['create_user']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HardwareConnectionsViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Hardware_connections.objects.all()
    serializer_class = serializers.HardwareConnectionsSerializer
    filter_backends = (
        DjangoFilterBackend,
        DynamicSearchFilter,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['create_user']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
