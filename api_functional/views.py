from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Cities
from .serializers import *


class CitiesView(ListAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class StreetsView(ListAPIView):
    def get_queryset(self):
        queryset = Streets.objects.filter(city=self.kwargs['city_id'])
        return queryset

    serializer_class = StreetsSerializer


class ShopCreateView(CreateAPIView):
    queryset = Shops.objects.all()

    serializer_class = ShopsSerializer
