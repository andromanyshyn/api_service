from django.urls import path
from . import views
urlpatterns = [
    path('city/', views.CitiesView.as_view(), name='cities'),
    path('<int:city_id>/street', views.StreetsView.as_view(), name='streets'),
    path('shop/', views.ShopListView.as_view(), name='shop'),
    # path('shop/<int:street>/<int:city>/<int:open>/',
    #      views.ShopListView.as_view(), name='shop_list'),
]
