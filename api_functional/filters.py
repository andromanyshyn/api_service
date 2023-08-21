from django.db.models import IntegerChoices
from django.utils import timezone

from django_filters import rest_framework as filters

from api_functional.models import Shops


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class WorkingHours(IntegerChoices):
    OPEN = 1, 'open'
    CLOSED = 0, 'close'


class ShopFilter(filters.FilterSet):
    city = CharFilterInFilter(field_name='city__name')
    street = CharFilterInFilter(field_name='street__name')
    open_shop = filters.NumberFilter(label='open', method='open_shop_filter')

    class Meta:
        model = Shops
        fields = ['city', 'street', 'open_shop']

    def open_shop_filter(self, queryset, key, value):
        current_time = timezone.now().time()
        if value == WorkingHours.OPEN.value:
            return queryset.filter(opening_time__lte=current_time.hour,
                                   closing_time__gt=current_time.hour)
        if value == WorkingHours.CLOSED.value:
            return queryset.filter(opening_time__gt=current_time.hour,
                                   closing_time__lte=current_time.hour)
        return queryset
