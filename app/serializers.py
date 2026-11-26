from rest_framework import serializers
from django.contrib.auth.models import User

from app.models import Genre, Actor, Play, TheatreHall, Performance, Reservation, Ticket


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = "__all__"


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = ("id", "title", "description")


class PlayListSerializer(PlaySerializer):
    genres = GenreSerializer(many=True, read_only=True)
    actors = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Play
        fields = ("id", "title", "description", "actors", "genres")


class TheatreHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheatreHall
        fields = "__all__"


class PerformanceSerializer(serializers.ModelSerializer):
    play = serializers.CharField(source="play.title", read_only=True)
    theatre_hall = serializers.CharField(source="theatre_hall.name", read_only=True)
    class Meta:
        model = Performance
        fields = ("id", "play", "theatre_hall", "show_time")


class PerformanceListSerializer(PerformanceSerializer):
    play = PlaySerializer(many=False, read_only=True)
    theatre_hall = TheatreHallSerializer(many=False, read_only=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Reservation
        fields = ("id", "user", "created_at")


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "row", "seat", "reservation", "performance")


class TicketListSerializer(TicketSerializer):
    reservation = ReservationSerializer(many=False, read_only=True)
    performance = PerformanceSerializer(many=False, read_only=True)