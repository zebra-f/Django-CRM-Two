import django_filters

from .models import Lead


class LeadListFilter(django_filters.FilterSet):
    first_name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Lead
        fields = {
            'age': ['lt', 'gt'],
        }
