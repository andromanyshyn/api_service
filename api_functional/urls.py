from django.urls import path
from . import views
urlpatterns = [
    path('cities/', views.CitiesView.as_view(), name='cities'),
    path('city/street/<int:city_id>/', views.StreetsView.as_view(), name='streets'),
    path('shop/', views.ShopListView.as_view(), name='shop')
]
