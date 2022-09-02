from django.urls import include, path
from rest_framework import routers

from .views import CastomUserViewSet

router = routers.DefaultRouter()
router.register(r'users', CastomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
