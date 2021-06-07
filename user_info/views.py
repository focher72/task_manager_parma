from django.contrib.auth.models import User, Group, Permission
from .serializers import UserSerializer, GroupSerializer, \
    PermissionSerializer, CurrentUserSerializer
from rest_framework import viewsets, permissions, filters as filtr
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .filters import UserFilter


"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (
        DjangoFilterBackend,
        UserFilter,
        # filters.SearchFilter,
        filters.OrderingFilter
    )
    # filterset_fields = ['id', 'username', 'first_name', 'email', 'groups', 'is_active']
    # search_fields = ['username', 'first_name', 'email']
    ordering_fields = ['is_active', 'groups', 'first_name']
    permission_classes = [permissions.IsAuthenticated]
"""


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-is_active', 'groups', 'first_name')
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend, filtr.OrderingFilter)
    filterset_class = UserFilter
    ordering_fields = ['is_active', 'groups', 'first_name']
    permission_classes = [permissions.IsAuthenticated]


@api_view()
@permission_classes([IsAuthenticated])
def current_user(request):
    serializer = CurrentUserSerializer(request.user)
    return JsonResponse(serializer.data)


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]
