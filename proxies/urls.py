from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProxyNodeViewSet, register_proxy, get_available_proxies

router = DefaultRouter()
router.register(r'proxies', ProxyNodeViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register-proxy/', register_proxy, name='register_proxy'),
    path('api/available-proxies/', get_available_proxies, name='available_proxies'),
]