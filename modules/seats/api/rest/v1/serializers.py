from rest_framework import serializers

from modules.domain.models import Seat


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'


class ReserveSerializer(serializers.Serializer):
    seat_list = serializers.ListField(
        child=serializers.IntegerField(),
    )

    def validate_seat_list(self, value):

        if len(value) == 0:
            raise serializers.ValidationError('Seat list cannot be empty')

        if Seat.objects.filter(id__in=value).count() != len(value):
            raise serializers.ValidationError('Invalid seat ID')

        if Seat.objects.filter(id__in=value).count() == 0:
            raise serializers.ValidationError('Seat not found')

        return value
