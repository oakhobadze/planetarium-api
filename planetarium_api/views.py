from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from .authentication import CustomTokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.settings import api_settings

from .models import Reservation, Ticket, ShowSession, PlanetariumDome, ShowTheme, AstronomyShow
from .serializers import (
    UserSerializer, ReservationSerializer, TicketSerializer,
    ShowSessionSerializer, PlanetariumDomeSerializer, ShowThemeSerializer, AstronomyShowSerializer
)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserRegister(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserLogin(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ReservationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        reservation, created = Reservation.objects.get_or_create(user=self.request.user)
        serializer.save(reservation=reservation)


class ShowSessionViewSet(viewsets.ModelViewSet):
    queryset = ShowSession.objects.all()
    serializer_class = ShowSessionSerializer
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class PlanetariumDomeViewSet(viewsets.ModelViewSet):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class ShowThemeViewSet(viewsets.ModelViewSet):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class AstronomyShowViewSet(viewsets.ModelViewSet):
    queryset = AstronomyShow.objects.all()
    serializer_class = AstronomyShowSerializer
    authentication_classes = (CustomTokenAuthentication,)
    permission_classes = (IsAuthenticated,)
