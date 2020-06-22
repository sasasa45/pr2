from django_filters import FilterSet, RangeFilter, BooleanFilter, ChoiceFilter,CharFilter, AllValuesMultipleFilter, AllValuesFilter
from django import forms
from .models import Items
from django.db.models import Q
brands=(
        ('Huawei','Huawei'),
        ('Apple','Apple'),
        ('Samsung','Samsung'),
)
class CategoryFilter(FilterSet):
    search=CharFilter(label='Search',method='sear', )
    price=RangeFilter(field_name='price')
    available=BooleanFilter(label='Available',field_name='quantity',widget=forms.CheckboxInput,method='avail')
    def avail(self, queryset, name, value):
        asa='__'.join([name,'gt'])
        if value:
            return queryset.filter(**{asa:0})
        else:
            return queryset
    def sear(self, queryset, name, value):
        if value:
            return queryset.filter(Q(name__icontains=value)|Q(text__icontains=value))
        else:
            return queryset
    def sear(self, queryset, name, value):
        if value:
            return queryset.filter(Q(name__icontains=value))
        else:
            return queryset
    class Meta:
        model=Items
        fields=['search','price','available', ]
class SearchFilter(FilterSet):
    search=CharFilter(label='Search',method='sea', )
    category=AllValuesMultipleFilter(field_name='category__name', )
    price=RangeFilter(field_name='price',)
    def sea(self, queryset, name, value):
        if value and len(value)>2:
            return Items.objects.search(value)
        else:
            return Items.objects.none()
    class Meta:
        model=Items
        fields=['search','category','price']
# <a href='{{referer}}&category={{categ}}'>
