from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from .models import Cities
from .filters import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class CitiesView(ListAPIView):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class StreetsView(ListAPIView):
    def get_queryset(self):
        queryset = Streets.objects.filter(city=self.kwargs['city_id'])
        return queryset

    serializer_class = StreetsSerializer


# class ShopCreateView(ListCreateAPIView):
#     queryset = Shops.objects.all()
#
#     serializer_class = ShopsSerializer


class ShopListView(ListAPIView):
    queryset = Shops.objects.all()

    filter_backends = (DjangoFilterBackend, )
    filterset_class = ShopFilter
    serializer_class = ShopListSerializer
