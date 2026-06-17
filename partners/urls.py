# partner_system_prototype/partners/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SectionViewSet, CardViewSet

router = DefaultRouter()
router.register(r'sections', SectionViewSet)
router.register(r'cards', CardViewSet)

urlpatterns = [
    path('', include(router.urls)),
]