from django.db import models
from django.contrib.auth.models import User


class Actor(models.Model):
    first_name = models.CharField(max_length=255, null=False, blank=False, default="")
    last_name = models.CharField(max_length=255, null=False, blank=False, default="")

    def __str__(self):
        return (self.first_name or "") + " " + (self.last_name or "")


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Play(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="plays")
    genres = models.ManyToManyField(Genre, related_name="plays")

    def __str__(self):
        return self.title


class TheatreHall(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE, related_name="performances")
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.CASCADE, related_name="performances")
    show_time = models.DateTimeField()

    def __str__(self):
        return f"{self.play.title} - {self.show_time}"


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reservation by {self.user}"


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE, related_name="tickets")
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="tickets")

    def __str__(self):
        return f"Row {self.row}, Seat {self.seat}"
