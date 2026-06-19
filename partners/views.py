# partners/views.py (добавьте это к уже существующим ViewSets)
from django.shortcuts import render
from .models import Section, Card
from rest_framework import viewsets # Оставьте импорты для API
from .serializers import SectionSerializer, CardSerializer # Оставьте импорты для API

# View для отображения партнерской системы с помощью шаблонов Django
def partners_ui_view(request):
    # Получаем все разделы, предзагружая связанные карточки для оптимизации (одним запросом)
    sections = Section.objects.prefetch_related('cards').all()
    return render(request, 'partners/partners_list.html', {'sections': sections})

# Ваши ViewSets для API DRF остаются здесь
class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer