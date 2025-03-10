from django.contrib import admin
from .models import Reservation, Ticket, ShowSession, PlanetariumDome, ShowTime, AstronomyShow

admin.site.register(Reservation)
admin.site.register(Ticket)
admin.site.register(ShowSession)
admin.site.register(PlanetariumDome)
admin.site.register(ShowTime)
admin.site.register(AstronomyShow)
