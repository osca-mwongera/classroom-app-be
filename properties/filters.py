import django_filters as filters
from django.db.models import Q

from geodata.models import County
from . models import Property

CHOICES = (
    ('ascending', 'Ascending'),
    ('descending', 'Descending')
)

class PropertyFilter(filters.FilterSet):
    name = filters.CharFilter(method='keyword_filter')
    county = filters.CharFilter(method='county_filter')

    # facilities = filters.ModelMultipleChoiceFilter(field_name='description', lookup_expr='icontains')
    # category = filters.ModelChoiceFilter(field_name='category', lookup_expr='icontains')

    min_area = filters.NumberFilter(field_name='area', lookup_expr='gte')
    max_area = filters.NumberFilter(field_name='area', lookup_expr='lte')
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')

    ordering = filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_ordering')

    class Meta:
        model = Property
        fields = [
            'categories',
            'facilities',
            'min_area',
            'max_area',
            'min_price',
            'max_price'
        ]

    def keyword_filter(self, queryset, name, value):
        qs = queryset.filter(
            Q(name__icontains=value)|
            Q(description__icontains=value)
        )

        return qs

    def county_filter(self, queryset, name, value):
        cnty = County.objects.filter(county_nam__icontains=value)[0]
        qs = queryset.filter(location__within=cnty.geom)

        return qs


    def filter_by_order(self, queryset, name, value):
        expression = 'created' if value == 'ascending' else '-created'
        return queryset.order_by(expression)