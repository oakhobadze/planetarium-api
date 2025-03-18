from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Reservation, Ticket, ShowSession, PlanetariumDome, ShowTheme, AstronomyShow


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password", "is_staff")
        read_only_fields = ("id", "is_staff")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()

        return user


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
    show_session = serializers.PrimaryKeyRelatedField(queryset=ShowSession.objects.all())

    class Meta:
        model = Ticket
        fields = ['id', 'row', 'seat', 'show_session', 'reservation']

    def get_reservation(self, obj):
        return obj.reservation.user.username

    def validate(self, data):
        row = data.get('row')
        seat = data.get('seat')
        show_session = data.get('show_session')

        if not show_session:
            raise serializers.ValidationError("You need to select a session")

        planetarium_dome = show_session.planetarium_dome

        if row is not None and (row < 1 or row > planetarium_dome.rows):
            raise serializers.ValidationError(f"Row must be from 1 to {planetarium_dome.rows}.")

        if seat is not None and (seat < 1 or seat > planetarium_dome.seats_in_row):
            raise serializers.ValidationError(f"Seat must be from 1 to {planetarium_dome.seats_in_row}.")

        if Ticket.objects.filter(show_session=show_session, row=row, seat=seat).exists():
            raise serializers.ValidationError("This seat is already booked for the selected session.")

        return data


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

