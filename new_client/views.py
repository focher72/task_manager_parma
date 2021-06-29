from .serializers import NewClientSerializer, ClientAdressSerializer, \
    NewClientReadSerializer, AdressAndCleintSerializer
from .models import New_client, Client_adress
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from django_filters import rest_framework as dj_filters
from .filters import NewClientFilter


class NewClientViewSet(viewsets.ModelViewSet):
    """Новые желающие на подключение"""
    queryset = New_client.objects.all().order_by('-create_date')
    serializer_class = NewClientSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['create_user', 'adress']
    search_fields = ['fio', 'contact', 'adress__street', 'adress__house']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class NewClientReadViewSet(viewsets.ReadOnlyModelViewSet):
    """Новые желающие на подключение"""
    queryset = New_client.objects.all().order_by('-create_date')
    serializer_class = NewClientReadSerializer
    filter_backends = (
        # DjangoFilterBackend,
        dj_filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    # filterset_fields = ['create_user', 'adress']
    filterset_class = NewClientFilter
    search_fields = ['fio', 'contact', 'adress__street', 'adress__house']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdressViewSet(viewsets.ModelViewSet):
    """Адреса желающих на подключение"""
    queryset = Client_adress.objects.all().order_by('street', 'house')
    serializer_class = ClientAdressSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['street', 'house']
    search_fields = ['street', 'house']
    ordering_fields = ['street']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AdressAndClientViewSet(viewsets.ReadOnlyModelViewSet):
    """Адреса желающих на подключение"""
    queryset = Client_adress.objects.all().order_by('street', 'house')
    serializer_class = AdressAndCleintSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['street', 'house']
    search_fields = ['street', 'house']
    ordering_fields = ['street']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
