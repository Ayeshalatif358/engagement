from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BlessingViewSet

router = DefaultRouter()
router.register(r'blessings', BlessingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]