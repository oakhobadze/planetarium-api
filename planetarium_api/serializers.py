from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Reservation, Ticket, ShowSession, PlanetariumDome, ShowTheme, AstronomyShow


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class NestedTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['row', 'seat', 'show_session']


class ReservationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    reserved_tickets = NestedTicketSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ['id', 'created_at', 'user', 'reserved_tickets']


class TicketSerializer(serializers.ModelSerializer):
    reservation = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ['id', 'row', 'seat', 'show_session', 'reservation']

    def get_reservation(self, obj):
        return obj.reservation.user.username


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = ['id', 'name', 'rows', 'seats_in_row']


class ShowThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTheme
        fields = ['id', 'name']


class AstronomyShowSerializer(serializers.ModelSerializer):
    show_themes = serializers.SlugRelatedField(slug_field='name', queryset=ShowTheme.objects.all(), many=True)

    class Meta:
        model = AstronomyShow
        fields = ['id', 'title', 'description', 'show_themes']


class ShowSessionSerializer(serializers.ModelSerializer):
    astronomy_show = serializers.SlugRelatedField(slug_field='title', queryset=AstronomyShow.objects.all())
    planetarium_dome = serializers.SlugRelatedField(slug_field='name', queryset=PlanetariumDome.objects.all())

    class Meta:
        model = ShowSession
        fields = ['id', 'astronomy_show', 'planetarium_dome', 'show_time']

