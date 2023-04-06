from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response

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


class ShopListView(ListCreateAPIView):
    queryset = Shops.objects.all()

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ShopFilter
    serializer_class = ShopListSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data['id'], status=status.HTTP_201_CREATED, headers=headers)
