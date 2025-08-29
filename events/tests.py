from django.test import TestCase
from .models import Event, Participant, Category
from django.utils import timezone
from datetime import timedelta

class EventModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Conference", description="A formal meeting.")
        self.event = Event.objects.create(
            name="DjangoCon",
            description="A conference for Django enthusiasts.",
            date=timezone.now().date() + timedelta(days=10),
            time="10:00",
            location="Online",
            category=self.category
        )

    def test_event_creation(self):
        self.assertEqual(self.event.name, "DjangoCon")
        self.assertEqual(self.event.description, "A conference for Django enthusiasts.")
        self.assertEqual(self.event.category.name, "Conference")

    def test_event_str(self):
        self.assertEqual(str(self.event), "DjangoCon")

class ParticipantModelTest(TestCase):

    def setUp(self):
        self.event = Event.objects.create(
            name="DjangoCon",
            description="A conference for Django enthusiasts.",
            date=timezone.now().date() + timedelta(days=10),
            time="10:00",
            location="Online",
            category=Category.objects.create(name="Conference", description="A formal meeting.")
        )
        self.participant = Participant.objects.create(name="John Doe", email="john@example.com")
        self.participant.events.add(self.event)

    def test_participant_creation(self):
        self.assertEqual(self.participant.name, "John Doe")
        self.assertEqual(self.participant.email, "john@example.com")
        self.assertIn(self.event, self.participant.events.all())

class CategoryModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Workshop", description="Hands-on sessions.")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Workshop")
        self.assertEqual(self.category.description, "Hands-on sessions.")

class EventViewTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name="Conference", description="A formal meeting.")
        self.event = Event.objects.create(
            name="DjangoCon",
            description="A conference for Django enthusiasts.",
            date=timezone.now().date() + timedelta(days=10),
            time="10:00",
            location="Online",
            category=self.category
        )

    def test_event_list_view(self):
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "DjangoCon")

    def test_event_detail_view(self):
        response = self.client.get(f'/events/{self.event.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "A conference for Django enthusiasts.")