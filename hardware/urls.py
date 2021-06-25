from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'ActiveHardware', views.ActiveHardwareViewSet,
                basename='ActiveHardware')
router.register(r'ActiveHardwareHistory', views.ActiveHardwareHistoryViewSet,
                basename='ActiveHardwareHistory')
router.register(r'ActiveHardwarePorts', views.ActiveHardwarePortsViewSet,
                basename='ActiveHardwarePorts')
router.register(r'Adress', views.AdressViewSet)
# router.register(r'HardwareAdress', views.HardwareAdressViewSet)
router.register(r'Vlan', views.VlanViewSet)
router.register(r'VlanPorts', views.VlanPortsViewSet, basename='VlanPorts')
router.register(r'HardwarePorts', views.HardwarePortsViewSet)
router.register(r'HardwarePortsVlan', views.HardwarePortsVlanViewSet, basename="PortsVlan")
router.register(r'HardwareConnections', views.HardwareConnectionsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('change_hardware', views.change_hardware),
]
