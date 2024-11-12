import django_filters

from shop.models import Product, Category


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    price = django_filters.NumberFilter(label='Price', field_name='price', lookup_expr='exact')
    description = django_filters.CharFilter(lookup_expr='icontains', label='Description')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Category',empty_label="Select a category")
    is_available = django_filters.BooleanFilter(label='Available')

    class Meta:
        model = Product
        fields = ['name','price', 'description','category', 'is_available', ]
