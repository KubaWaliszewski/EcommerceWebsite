import django_filters
from django.db.models import Q

from shop.infrastructure.orm.models import Product


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')

    class Meta:
        model = Product
        fields = ['name', ]