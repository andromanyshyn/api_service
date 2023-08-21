from django.contrib import admin
from api_functional.models import Cities, Streets, Shops


@admin.register(Cities)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Streets)
class StreetAdmin(admin.ModelAdmin):
    pass


@admin.register(Shops)
class ShopAdmin(admin.ModelAdmin):
    pass