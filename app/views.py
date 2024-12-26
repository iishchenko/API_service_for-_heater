from rest_framework.viewsets import ModelViewSet
from app.models import Actor, Genre, Play, TheatreHall, Performance, Reservation, Ticket
from app.serializers import (
    ActorSerializer,
    GenreSerializer,
    PlaySerializer,
    TheatreHallSerializer,
    PerformanceSerializer,
    ReservationSerializer,
    TicketSerializer,
)


class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class PlayViewSet(ModelViewSet):
    queryset = Play.objects.all()
    serializer_class = PlaySerializer


class TheatreHallViewSet(ModelViewSet):
    queryset = TheatreHall.objects.all()
    serializer_class = TheatreHallSerializer


class PerformanceViewSet(ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer


class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class TicketViewSet(ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
