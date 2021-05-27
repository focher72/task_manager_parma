from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from task_manager import urls as tm_url
from task_manager.views import index
from hardware import urls as hw_url
from user_info import urls as ui_url
from oracle_base.views import ClientListSet, ClientShpdInfoSet
from new_client.views import NewClientViewSet
from django.conf import settings
from django.conf.urls.static import static
from changelog.views import ChangeLogViewSet


router = routers.DefaultRouter()

router.register(r'ClientList', ClientListSet)
router.register(r'ClientShpdInfo', ClientShpdInfoSet)
router.register(r'NewClient', NewClientViewSet)
router.register(r'changelog', ChangeLogViewSet)


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('router/', include(router.urls)),
    path('task_manager/', include(tm_url)),
    path('hardware/', include(hw_url)),
    path('user_info/', include(ui_url)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
