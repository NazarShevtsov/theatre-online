from django.contrib import admin

from app.models import Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name",)
    list_filter = ("first_name", "last_name",)


@admin.register(Play)
class PlayAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(TheatreHall)
class TheatreHallAdmin(admin.ModelAdmin):
    list_display = ("name", "rows", "seats_in_row")


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ("play", "theatre_hall", "show_time")
    list_filter = ("theatre_hall", "show_time")


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ("user", "created_at")


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("performance", "row", "seat")

