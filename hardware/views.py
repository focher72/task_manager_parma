from hardware import models, serializers
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse
# from .services import _change_hardware_adress, _change_hardware_ports
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from django_filters import rest_framework as dj_filters
from . import filters as drf_filters
from simple_history.utils import update_change_reason


"""
@api_view()
@permission_classes([IsAdminUser])
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
"""


class ActiveHardwareViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Active_hardware.objects.all()
    serializer_class = serializers.ActiveHardwareSerializer
    filter_backends = (
        dj_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    )
    filterset_class = drf_filters.ActiveHardwareFilter
    ordering_fields = ['name_hardware', 'serial_num', 'ip_adress']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        instance = serializer.save()
        try:
            update_change_reason(instance, self.request.data['comment'])
        except KeyError:
            update_change_reason(instance, 'Пусто')

    def perform_create(self, serializer):
        instance = serializer.save()
        update_change_reason(instance, 'create [AUTO]')

    def perform_destroy(self, instance):
        instance.delete()
        try:
            update_change_reason(instance, self.request.data['comment'])
        except KeyError:
            update_change_reason(instance, 'Пусто')


class ActiveHardwareHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Все заявки"""
    queryset = models.Active_hardware_history.objects.all()
    serializer_class = serializers.ActiveHardwareHistorySerializer
    filter_backends = (
        dj_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    )
    filterset_class = drf_filters.ActiveHardwareHistoryFilter
    ordering_fields = ['name_hardware', 'serial_num', 'ip_adress']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ActiveHardwarePortsViewSet(viewsets.ReadOnlyModelViewSet):
    """Все заявки"""
    queryset = models.Active_hardware.objects.all()
    serializer_class = serializers.ActiveHardwarePortsSerializer
    filter_backends = (
        dj_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    )
    #filterset_class = drf_filters.ActiveHardwareHistoryFilter
    ordering_fields = ['name_hardware', 'serial_num', 'ip_adress']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdressViewSet(viewsets.ModelViewSet):
    """ Адреса оборудования или узлы """
    queryset = models.Hardware_adress.objects.all()
    serializer_class = serializers.HardwareAdressSerializer
    filter_backends = (
        dj_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    )
    filterset_class = drf_filters.HardwareAdressFilter
    ordering_fields = ['adress', 'comment']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VlanViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Vlan.objects.all()
    serializer_class = serializers.VlanSerializer
    filter_backends = (
        dj_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    )
    filterset_class = drf_filters.VlanFilter
    ordering_fields = ['vlan_number', 'vlan_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VlanPortsViewSet(viewsets.ReadOnlyModelViewSet):
    """Все заявки"""
    queryset = models.Vlan.objects.all()
    serializer_class = serializers.VlanPortsSerializer
    filter_backends = (
        dj_filters.DjangoFilterBackend,
        filters.OrderingFilter,
    )
    filterset_class = drf_filters.VlanFilter
    ordering_fields = ['vlan_number', 'vlan_name']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HardwarePortsViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Hardware_ports.objects.all()
    serializer_class = serializers.PortsSerializer
    filter_backends = (
        dj_filters.DjangoFilterBackend,
        filters.OrderingFilter
    )
    filterset_class = drf_filters.PortsFilter
    ordering_fields = ['hardware']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HardwarePortsVlanViewSet(viewsets.ReadOnlyModelViewSet):
    """Все заявки"""
    queryset = models.Hardware_ports.objects.all()
    serializer_class = serializers.PortsVlanSerializer
    filter_backends = (
        dj_filters.DjangoFilterBackend,
        filters.OrderingFilter
    )
    filterset_class = drf_filters.PortsFilter
    ordering_fields = ['hardware']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class HardwareConnectionsViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Hardware_connections.objects.all()
    serializer_class = serializers.HardwareConnectionsSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['create_user']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
