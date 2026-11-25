from django.contrib.auth.models import User
from django.db import models
from django.db.models.constraints import UniqueConstraint


class Genre(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(null=False, blank=False, max_length=100)
    last_name = models.CharField(null=False, blank=False, max_length=255)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"



class Play(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor, related_name="plays")
    genres = models.ManyToManyField(Genre, related_name="plays")

    def __str__(self) -> str:
        return self.title


class TheatreHall(models.Model):
    name = models.CharField(unique=True, max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self) -> str:
        return self.name


class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name="performances")
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.CASCADE, related_name="performances")
    show_time = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.play} at {self.show_time} in {self.theatre_hall}"


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Created a reservation by {self.user} at {self.created_at}"


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    class Meta:
        constraints = [UniqueConstraint(
            fields=["seat", "row", "performance"],
            name="unique_seat_in_row"
        )]