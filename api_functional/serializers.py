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


class ShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shops
        fields = (
            'id',
            'name',
            'city',
            'street',
            'house',
        )
        extra_kwargs = {
            'name': {'write_only': True},
            'city': {'write_only': True},
            'street': {'write_only': True},
            'house': {'write_only': True},
            'id': {'read_only': True},
        }


class ShopListSerializer(serializers.ModelSerializer):
    city = serializers.SlugRelatedField(slug_field='name', read_only=True)
    street = serializers.SlugRelatedField(slug_field='name', read_only=True)

    class Meta:
        model = Shops
        fields = (
            'name',
            'city',
            'street',
            'house',
            'opening_time',
            'closing_time',
        )
