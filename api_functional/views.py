from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.response import Response

from api_functional.models import Cities, Streets, Shops
from api_functional.filters import ShopFilter
from api_functional.serializers import ShopListSerializer, CitiesSerializer, StreetsSerializer
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
        response = super().create(request, *args, *kwargs)
        return Response(response.data['id'], status=response.status_code, headers=response.headers)
