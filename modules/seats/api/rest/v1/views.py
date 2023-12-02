from datetime import timedelta

from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.views import extend_schema
from rest_framework import (decorators, exceptions, response, status, views,
                            viewsets)
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny, IsAuthenticated

from modules.domain.models import Match, Reservation, Seat, Stadium
from modules.seats.api.rest.v1.filters import SeatFilter
from modules.seats.api.rest.v1.serializers import (ReserveSerializer,
                                                   SeatSerializer)


class SeatViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Seat.objects.all()
    permission_classes = [AllowAny]
    serializer_class = SeatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SeatFilter
    parser_classes = [JSONParser]


class ReserveApiView(views.APIView):
    queryset = Seat.objects.all()
    permission_classes = [IsAuthenticated]
    parser_classes = [JSONParser]

    @extend_schema(request=ReserveSerializer)
    def post(self, request, match_id):
        try:
            serializer = ReserveSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            match = Match.objects.get(pk=match_id)
            stadium = Stadium.objects.get(match=match)
            if not Seat.objects.filter(stadium=stadium, is_reserved=False).exists():
                raise exceptions.NotFound(detail="seat not found")
            message = self.reserve_seats(request.user, match, serializer.data['seat_list'])
            return response.Response({"message": message}, status=status.HTTP_200_OK)
        except Match.DoesNotExist:
            return response.Response(details="Match not found", status=status.HTTP_404_NOT_FOUND)

    @staticmethod
    def reserve_seats(user, match, selected_seats):
        current_time = timezone.now()
        expiry_time = current_time + timedelta(minutes=5)  # Example: reservation expires in 5 minutes
        reservation = Reservation.objects.create(user=user, match=match, expiry_time=expiry_time)
        reservation.seats.add(*selected_seats)
        Seat.objects.filter(id__in=selected_seats).update(is_reserved=True)
        return "you have 5 minutes to pay otherwise it will expired"
