    # partner_system_prototype/partners/serializers.py
from rest_framework import serializers
from .models import Section, Card

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__' # Включаем все поля модели

class SectionSerializer(serializers.ModelSerializer):
    # Опционально: можно вложить сериализатор карточек, чтобы получать их вместе с разделом
    # cards = CardSerializer(many=True, read_only=True)
    class Meta:
        model = Section
        fields = '__all__' # Включаем все поля модели