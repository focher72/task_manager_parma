from oracle_base import models, serializers
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class ClientListSet(viewsets.ReadOnlyModelViewSet):
    """Полная информация о всех заявках"""
    queryset = models.Client_lists.objects.all()
    serializer_class = serializers.ClientListSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )
    filterset_fields = ['clnt_type']
    search_fields = ['clnt_name', 'abonent_adr']
    ordering_fields = ['clnt_name', 'abonent_adr']
    permission_classes = [permissions.IsAuthenticated]


class ClientShpdInfoSet(viewsets.ReadOnlyModelViewSet):
    """Полная информация о всех заявках"""
    queryset = models.Client_shpd_info.objects.all()
    serializer_class = serializers.ClientShpdInfoSerializer
    permission_classes = [permissions.IsAuthenticated]
