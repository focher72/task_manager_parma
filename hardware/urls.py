from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'ActiveHardware', views.ActiveHardwareViewSet,
                basename='ActiveHardware')
router.register(r'Adress', views.AdressViewSet)
router.register(r'ChangeReason', views.ChangeReasonViewSet)
router.register(r'HardwareAdress', views.HardwareAdressViewSet)
router.register(r'Vlan', views.VlanViewSet)
router.register(r'VlanRead', views.VlanReadViewSet, basename='VlanRead')
router.register(r'HardwarePorts', views.HardwarePortsViewSet)
router.register(r'HardwareConnections', views.HardwareConnectionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('change_hardware', views.change_hardware),
]
