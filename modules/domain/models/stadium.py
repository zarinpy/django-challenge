from django.db import models
from modules.common.models import TimestampedModelMixin


class Stadium(TimestampedModelMixin):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Match(TimestampedModelMixin):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    match_date = models.DateTimeField()
    opponents = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.opponents} at {self.stadium.name}"


class Ticket(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.IntegerField()

    def __str__(self):
        return f"Ticket for {self.match.opponents}"


class Seat(TimestampedModelMixin):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    row = models.CharField(max_length=5)
    section = models.CharField(max_length=20)
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Seat {self.seat_number} in {self.section} - Row {self.row}"


class Reservation(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    seats = models.ManyToManyField(Seat)
    expiry_time = models.DateTimeField()

    def __str__(self):
        return f"Reservation for {self.user.username} at {self.match.opponents}"


class Basket(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    tickets = models.ManyToManyField(Ticket)
    seats = models.ManyToManyField(Seat)
    created_at = models.DateTimeField(auto_now_add=True)
