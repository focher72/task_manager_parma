from django_filters import rest_framework as filters
from .models import New_client
from django.db import models as django_models


class NewClientFilter(filters.FilterSet):
    start_date = filters.DateTimeFilter(field_name="create_date", lookup_expr='gte')
    end_date = filters.DateTimeFilter(field_name="create_date", lookup_expr='lte')

    class Meta:
        model = New_client
        fields = ['create_user', 'adress']

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': filters.IsoDateTimeFilter
        },
    }
