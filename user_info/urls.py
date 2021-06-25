from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user_list')
router.register(r'users_pass', views.UserPassViewSet, basename='user_pass_list')
router.register(r'groups', views.GroupViewSet)
router.register(r'Permission', views.PermissionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('current_user/', views.current_user),
]
