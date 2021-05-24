from .serializers import NewClientSerializer
from .models import New_client
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend


class NewClientViewSet(viewsets.ModelViewSet):
    """Новые желающие на подключение"""
    queryset = New_client.objects.all()
    serializer_class = NewClientSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['create_user']
    search_fields = ['fio', 'contact']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
