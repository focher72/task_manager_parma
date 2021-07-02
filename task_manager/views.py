from task_manager import models, service, serializers
from rest_framework import permissions, viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse


def index(request):
    text = 'parmatel'
    return HttpResponse(text, content_type='text/plain; charset=utf-8')


class TaskViewSet(viewsets.ModelViewSet):
    """Все заявки"""
    queryset = models.Task.objects.all()
    serializer_class = serializers.TaskSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['source', 'type']
    search_fields = ['task_text']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TechTaskFullViewSet(viewsets.ReadOnlyModelViewSet):
    """Полная информация о всех заявках"""
    queryset = models.Task.objects.filter(category='tech')
    serializer_class = serializers.TaskFullInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AbonTaskFullViewSet(viewsets.ReadOnlyModelViewSet):
    """Полная информация о всех заявках"""
    queryset = models.Task.objects.filter(category='abon')
    serializer_class = serializers.TaskFullInfoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaskStatusViewSet(viewsets.ModelViewSet):
    """история статусов заявок"""
    queryset = models.Task_status.objects.all()
    serializer_class = serializers.TaskStatusSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['status', 'task']
    search_fields = ['task']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaskUserViewSet(viewsets.ModelViewSet):
    """Исполнители заявок"""
    queryset = models.Task_user_work.objects.all()
    serializer_class = serializers.TaskUserWorkSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['user', 'task']
    search_fields = ['task']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaskMessagesViewSet(viewsets.ModelViewSet):
    """Сообщения от сотрудников заявок"""
    queryset = models.Task_messages.objects.all()
    serializer_class = serializers.TaskMessagesSerializer
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
    filterset_fields = ['task']
    search_fields = ['task']
    ordering_fields = ['create_date']
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StatusViewSet(viewsets.ModelViewSet):
    """Все доступные статусы"""
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaskSourceViewSet(viewsets.ModelViewSet):
    """Источники заявок"""
    queryset = models.Task_source.objects.all()
    serializer_class = serializers.TaskSourceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TaskTypesViewSet(viewsets.ModelViewSet):
    """Типы заявок"""
    queryset = models.Task_types.objects.all()
    serializer_class = serializers.TaskTypesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TechTaskTypesViewSet(viewsets.ReadOnlyModelViewSet):
    """Типы заявок"""
    queryset = models.Task_types.objects.filter(category='tech')
    serializer_class = serializers.TaskTypesReadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AbonTaskTypesViewSet(viewsets.ReadOnlyModelViewSet):
    """Типы заявок"""
    queryset = models.Task_types.objects.filter(category='abon')
    serializer_class = serializers.TaskTypesReadSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
