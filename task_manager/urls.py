from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'task_list', views.TaskViewSet, basename='task_list')
router.register(r'task_full_info', views.TaskFullViewSet,
                basename='task_full_info')
router.register(r'task_user', views.TaskUserViewSet)
router.register(r'task_status', views.TaskStatusViewSet)
router.register(r'task_messages', views.TaskMessagesViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
