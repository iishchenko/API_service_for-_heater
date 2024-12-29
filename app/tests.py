from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from app.models import Actor, Genre, Play, TheatreHall, Performance, Reservation, Ticket
from rest_framework.authtoken.models import Token
from django.utils.timezone import now


class ActorModelTest(TestCase):
    def test_actor_creation(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.assertEqual(str(actor), "John Doe")


class GenreModelTest(TestCase):
    def test_genre_creation(self):
        genre = Genre.objects.create(name="Drama")
        self.assertEqual(str(genre), "Drama")


class PlayModelTest(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.genre = Genre.objects.create(name="Comedy")

    def test_play_creation(self):
        play = Play.objects.create(title="Test Play", description="A great play")
        play.actors.add(self.actor)
        play.genres.add(self.genre)
        self.assertEqual(str(play), "Test Play")
        self.assertIn(self.actor, play.actors.all())
        self.assertIn(self.genre, play.genres.all())


class TheatreHallModelTest(TestCase):
    def test_theatre_hall_creation(self):
        hall = TheatreHall.objects.create(name="Main Hall", rows=10, seats_in_row=20)
        self.assertEqual(str(hall), "Main Hall")


class ActorAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.actor_data = {"first_name": "John", "last_name": "Doe"}
        user = User.objects.create_user(username='testuser', password='testpass')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_create_actor(self):
        response = self.client.post("/api/actors/", self.actor_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["first_name"], "John")

    def test_get_actors(self):
        Actor.objects.create(**self.actor_data)
        response = self.client.get("/api/actors/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)


class PlayAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.actor = Actor.objects.create(first_name="John", last_name="Doe")
        self.genre = Genre.objects.create(name="Drama")
        self.play_data = {
            "title": "Hamlet",
            "description": "A Shakespeare play",
            "actors": [self.actor.id],
            "genres": [self.genre.id],
        }
        user = User.objects.create_user(username='testuser', password='testpass')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_create_play(self):
        response = self.client.post("/api/plays/", self.play_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Hamlet")


class PerformanceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.play = Play.objects.create(title="Test Play", description="A play")
        self.hall = TheatreHall.objects.create(name="Main Hall", rows=10, seats_in_row=20)
        self.performance_data = {
            "play": self.play.id,
            "theatre_hall": self.hall.id,
            "show_time": now(),
        }
        user = User.objects.create_user(username='testuser', password='testpass')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_create_performance(self):
        response = self.client.post("/api/performances/", self.performance_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["play"], self.play.id)


class TicketAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="testuser", password="password")
        self.play = Play.objects.create(title="Test Play", description="A play")
        self.hall = TheatreHall.objects.create(name="Main Hall", rows=10, seats_in_row=20)
        self.performance = Performance.objects.create(
            play=self.play, theatre_hall=self.hall, show_time=now()
        )
        self.reservation = Reservation.objects.create(user=self.user)
        self.ticket_data = {
            "row": 1,
            "seat": 2,
            "performance": self.performance.id,
            "reservation": self.reservation.id,
        }
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_create_ticket(self):
        response = self.client.post("/api/tickets/", self.ticket_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["row"], 1)
        self.assertEqual(response.data["seat"], 2)
