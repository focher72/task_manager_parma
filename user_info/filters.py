from django_filters import rest_framework as filters
from django.contrib.auth.models import User


class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['icontains', 'exact', 'startswith'],
            'email': ['icontains', 'exact'],
            'first_name': ['icontains', 'exact'],
            'is_active': ['exact'],
            'groups': ['exact'],
        }
