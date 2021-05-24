from changelog.models import ChangeLog
from changelog.serializers import ChangeLogSerializer
from rest_framework import permissions
from rest_framework import viewsets


class ChangeLogViewSet(viewsets.ReadOnlyModelViewSet):
    """Все заявки"""
    queryset = ChangeLog.objects.all()
    serializer_class = ChangeLogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
