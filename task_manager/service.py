from django_filters import rest_framework as filter
from task_manager.models import Task_user_work, Task_status, Status, Task
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CharFilterInFilter(filter.BaseInFilter, filter.CharFilter):
    pass


class TaskUserFilter(filter.FilterSet):
    # task = CharFilterInFilter(field_name='task__task_text', lookup_expr='in')
    # user = CharFilterInFilter(field_name='', lookup_expr='in')

    class Meta:
        model = Task_user_work
        fields = ['task', 'user']


class TaskFilter(filter.FilterSet):

    class Meta:
        model = Task
        fields = ['id', 'source', 'type']


class TaskStatusFilter(filter.FilterSet):

    class Meta:
        model = Task_status
        fields = ['task', 'status']


class StatusFilter(filter.FilterSet):
    # status_name = CharFilterInFilter(field_name='', lookup_expr='in')

    class Meta:
        model = Status
        fields = ['status_name']


class PaginationTask(PageNumberPagination):
    page_size = 10
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
