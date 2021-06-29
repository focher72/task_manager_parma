from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewClientViewSet, AdressViewSet, NewClientReadViewSet, \
    AdressAndClientViewSet


router = DefaultRouter()
router.register(r'NewClient', NewClientViewSet, basename='NewClient')
router.register(r'NewClientRead', NewClientReadViewSet, basename='NewClientRead')
router.register(r'Adress', AdressViewSet, basename='Adress')
router.register(r'AdressAndClient', AdressAndClientViewSet, basename='AdressAndClient')


urlpatterns = [
    path('', include(router.urls)),
]
