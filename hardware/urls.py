from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'ActiveHardware', views.ActiveHardwareViewSet,
                basename='ActiveHardware')

urlpatterns = [
    path('', include(router.urls)),
    path('change_hardware', views.change_hardware),
]
