from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'Task', views.TaskViewSet, basename='Task')
router.register(r'TechTaskFullInfo', views.TechTaskFullViewSet,
                basename='TechTaskFullInfo')
router.register(r'AbonTaskFullInfo', views.AbonTaskFullViewSet,
                basename='AbonTaskFullInfo')
router.register(r'TaskUser', views.TaskUserViewSet)
router.register(r'TaskStatus', views.TaskStatusViewSet)
router.register(r'TaskMessages', views.TaskMessagesViewSet)
router.register(r'Status', views.StatusViewSet)
router.register(r'TaskSource', views.TaskSourceViewSet)
router.register(r'TaskTypes', views.TaskTypesViewSet,
                basename='TaskTypes')
router.register(r'TechTaskTypes', views.TechTaskTypesViewSet,
                basename='TechTaskTypes')
router.register(r'AbonTaskTypes', views.AbonTaskTypesViewSet,
                basename='AbonTaskTypes')


urlpatterns = [
    path('', include(router.urls)),
]
