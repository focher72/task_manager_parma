from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user_list')
router.register(r'groups', views.GroupViewSet)
router.register(r'Permission', views.PermissionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]