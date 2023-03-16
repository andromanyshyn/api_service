from django.contrib import admin
from .models import *


@admin.register(Cities)
class CityAdmin(admin.ModelAdmin):
    pass


@admin.register(Streets)
class StreetAdmin(admin.ModelAdmin):
    pass


@admin.register(Shops)
class ShopAdmin(admin.ModelAdmin):
    pass