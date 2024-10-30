import django_filters
from django.db.models import Q

from account.models import CustomUser
from shop.models import Product, Category
from orders.models import Order


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(method='filter_by_full_name', label='Full Name')
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email')
    
    class Meta:
        model = CustomUser
        fields = ['name', 'email', 'role',]

    def filter_by_full_name(self, queryset, name, value):
        return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value)
        )
    
class OrderFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email')
    
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'status', 'email',]
 


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')
    price = django_filters.NumberFilter(label='Price', field_name='price', lookup_expr='exact')
    description = django_filters.CharFilter(lookup_expr='icontains', label='Description')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), label='Category',empty_label="Select a category")
    is_available = django_filters.BooleanFilter(label='Available')

    class Meta:
        model = Product
        fields = ['name','price', 'description','category', 'is_available', ]


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains', label='Name')

    class Meta:
        model = Product
        fields = ['name', ]