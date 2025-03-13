from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, ReservationViewSet, TicketViewSet,
    ShowSessionViewSet, PlanetariumDomeViewSet,
    ShowThemeViewSet, AstronomyShowViewSet, UserLogin,
    ManageUserView, UserRegister
)

app_name = "planetarium"

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("reservations", ReservationViewSet)
router.register("tickets", TicketViewSet)
router.register("show_sessions", ShowSessionViewSet)
router.register("planetarium_domes", PlanetariumDomeViewSet)
router.register("show_themes", ShowThemeViewSet)
router.register("astronomy_shows", AstronomyShowViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", UserLogin.as_view(), name="user-login"),
    path("update_user/", ManageUserView.as_view(), name="update-user"),
    path("create_user/", UserRegister.as_view(), name="create-user"),
]
