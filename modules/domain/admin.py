from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from modules.domain.models import (Basket, Match, Reservation, Seat, Stadium,
                                   User)


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ["opponents", "stadium", "match_date"]


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name"]


@admin.register(Stadium)
class StadiumAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "capacity"]


@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):
    list_display = ["stadium", "seat_number", "row", "section"]


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["user", "expiry_time"]


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ["user", "created_at"]
