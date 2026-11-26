from django.shortcuts import render
from rest_framework import viewsets

from app.models import Genre, Actor, Play, TheatreHall, Performance, Reservation
from app.serializers import GenreSerializer, ActorSerializer, PlaySerializer, PlayListSerializer, TheatreHallSerializer, \
    PerformanceSerializer, PerformanceListSerializer, ReservationSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class PlayViewSet(viewsets.ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer

    def get_queryset(self):
        queryset = self.queryset
        if self.action == "list":
            return queryset.prefetch_related("genres", "actors")
        return queryset

    def get_serializer_class(self):
        if self.action == "list":
            return PlayListSerializer
        return PlaySerializer


class TheatreHallViewSet(viewsets.ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return PerformanceListSerializer
        return PerformanceSerializer

    def get_queryset(self):
        queryset = self.queryset

        if self.action == "list":
            return queryset.select_related("play", "theatre_hall")
        return queryset


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
