from django.urls import path
from . import views
urlpatterns = [
    path('city/', views.CitiesView.as_view(), name='cities'),
    path('<int:city_id>/street', views.StreetsView.as_view(), name='streets'),
    path('shop/', views.ShopCreateView.as_view(), name='shop')
]
