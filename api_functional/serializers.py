from rest_framework import serializers
from .models import *


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['name']


class StreetsSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Streets
        fields = ['name', 'city']


class ShopListSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', queryset=Cities.objects.all())
    street = serializers.SlugRelatedField(slug_field='name', queryset=Streets.objects.all())

    class Meta:
        model = Shops
        fields = (
            'id',
            'name',
            'city',
            'street',
            'house',
            'opening_time',
            'closing_time',
        )
