from django.shortcuts import render

# Create your views here.
# partner_system_prototype/partners/views.py
from rest_framework import viewsets
from .models import Section, Card
from .serializers import SectionSerializer, CardSerializer

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer