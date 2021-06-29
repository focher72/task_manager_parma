from django_filters import rest_framework as filters
from .models import New_client


class NewClientFilter(filters.FilterSet):

    class Meta:
        model = New_client
        fields = {
            # 'id': ['exact'],
            # 'ip_adress': ['icontains', 'exact'],
            # 'name_hardware': ['icontains', 'exact'],
            # 'serial_num': ['icontains', 'exact'],
            'create_date': ['range', 'gte'],
        }
