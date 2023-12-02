from django_filters import rest_framework as filters
from modules.domain.models import Seat, Stadium


class SeatFilter(filters.FilterSet):
    match_id = filters.NumberFilter(method='filter_by_match_id')

    class Meta:
        model = Seat
        fields = ['match_id']

    def filter_by_match_id(self, queryset, name, value):
        try:
            # Retrieve stadium associated with the match ID
            stadium = Stadium.objects.get(match__id=value)
            return queryset.filter(stadium=stadium, is_reserved=False)
        except Stadium.DoesNotExist:
            return queryset.none()
