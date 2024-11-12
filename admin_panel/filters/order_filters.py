import django_filters

from orders.models import Order


class OrderFilter(django_filters.FilterSet):
    email = django_filters.CharFilter(lookup_expr='icontains', label='Email')
    
    class Meta:
        model = Order
        fields = ['id', 'created_at', 'status', 'email',]