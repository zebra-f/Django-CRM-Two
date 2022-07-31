import django_filters

from .models import Lead


class LeadListFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Lead
        fields = {
            'email': ['icontains'],
            'phone': ['icontains'],
        }
