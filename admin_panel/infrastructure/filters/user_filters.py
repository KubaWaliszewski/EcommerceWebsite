import django_filters
from django.db.models import Q

from account.infrastructure.orm.models import CustomUser


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