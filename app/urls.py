from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import GenreViewSet, ActorViewSet, PlayViewSet, TheatreHallViewSet

router = DefaultRouter()
router.register("genres", GenreViewSet)
router.register("actors", ActorViewSet)
router.register("plays", PlayViewSet)
router.register("theatre-halls", TheatreHallViewSet)

urlpatterns = [
    path("", include(router.urls))
]

app_name = "app"