# core/urls.py
from django.contrib import admin
from django.urls import path, include
from partners.views import partners_ui_view # Импортируем наш новый View

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', partners_ui_view, name='partners_ui'), # Наша новая страница
    path('api/', include('partners.urls')), # URL-ы для REST API
]