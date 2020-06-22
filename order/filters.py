from django_filters import FilterSet, AllValuesMultipleFilter
from .models import Order
class OrderFilter(FilterSet):
    manager=AllValuesMultipleFilter(field_name='manager')
    class Meta:
        model=Order
        fields=['manager',]
