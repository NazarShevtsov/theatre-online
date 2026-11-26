from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import GenreViewSet, ActorViewSet, PlayViewSet, TheatreHallViewSet, PerformanceViewSet, \
    ReservationViewSet, TicketViewSet

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("plays", PlayViewSet)
router.register("theatre-halls", TheatreHallViewSet)
router.register("performances", PerformanceViewSet)
router.register("reservations", ReservationViewSet)
router.register("tickets", TicketViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "app"