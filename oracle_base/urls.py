from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register(r'ClientList', views.ClientListSet)
router.register(r'ClientShpdInfo', views.ClientShpdInfoSet)


urlpatterns = [
    path('', include(router.urls)),
]
