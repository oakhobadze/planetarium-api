from django.contrib.auth.models import User
from django.db import models


class Reservation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.created_at)


class Ticket(models.Model):
    row = models.IntegerField()
    seat = models.IntegerField()
    show_session = models.ForeignKey("ShowSession", on_delete=models.CASCADE, related_name="tickets")
    reservation = models.ForeignKey("Reservation", on_delete=models.CASCADE, related_name="reserved_tickets")

    def __str__(self):
        return f"{self.row}-{self.seat}-{self.reservation}"


class ShowSession(models.Model):
    astronomy_show = models.ForeignKey("AstronomyShow", on_delete=models.CASCADE)
    planetarium_dome = models.ForeignKey("PlanetariumDome", on_delete=models.CASCADE)
    show_time = models.DateTimeField()

    def __str__(self):
        return str(self.show_time)


class PlanetariumDome(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    def __str__(self):
        return self.name


class ShowTheme(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AstronomyShow(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    show_themes = models.ManyToManyField(ShowTheme, related_name="astronomy_shows")

    def __str__(self):
        return self.title
