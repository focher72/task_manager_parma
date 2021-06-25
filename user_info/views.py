from django.contrib.auth.models import User, Group, Permission
from .serializers import UserSerializer, GroupSerializer, \
    PermissionSerializer, CurrentUserSerializer, UserPassSerializer
from rest_framework import viewsets, permissions, filters
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as dj_filters
from .filters import UserFilter


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-is_active', 'groups', 'first_name')
    serializer_class = UserSerializer
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = UserFilter
    ordering_fields = ['is_active', 'groups', 'first_name']
    permission_classes = [permissions.IsAuthenticated]


class UserPassViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-is_active', 'groups', 'first_name')
    serializer_class = UserPassSerializer
    filter_backends = (dj_filters.DjangoFilterBackend, filters.OrderingFilter)
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
