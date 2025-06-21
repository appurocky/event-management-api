import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from events.models import Event, Attendee
from django.utils.timezone import make_aware
from datetime import datetime, timedelta

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def sample_event():
    return Event.objects.create(
        name="Test Event",
        location="Test City",
        start_time=make_aware(datetime.now() + timedelta(days=1)),
        end_time=make_aware(datetime.now() + timedelta(days=2)),
        max_capacity=2,
        timezone="Asia/Kolkata"
    )

def test_create_event(client):
    url = reverse('create_event')
    data = {
        "name": "My Event",
        "location": "Bangalore",
        "start_time": "2025-07-01T10:00:00Z",
        "end_time": "2025-07-01T12:00:00Z",
        "max_capacity": 100,
        "timezone": "Asia/Kolkata"
    }
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data["name"] == "My Event"

def test_register_attendee_success(client, sample_event):
    url = reverse('register_attendee', args=[sample_event.id])
    data = {"name": "Alice", "email": "alice@example.com"}
    response = client.post(url, data, format='json')
    assert response.status_code == 201
    assert response.data["name"] == "Alice"

def test_register_duplicate_email(client, sample_event):
    Attendee.objects.create(name="Bob", email="bob@example.com", event=sample_event)
    url = reverse('register_attendee', args=[sample_event.id])
    data = {"name": "Bob", "email": "bob@example.com"}
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert "already registered" in response.data["error"]

def test_register_event_full(client, sample_event):
    Attendee.objects.create(name="User1", email="u1@test.com", event=sample_event)
    Attendee.objects.create(name="User2", email="u2@test.com", event=sample_event)
    url = reverse('register_attendee', args=[sample_event.id])
    data = {"name": "User3", "email": "u3@test.com"}
    response = client.post(url, data, format='json')
    assert response.status_code == 400
    assert "Event is full" in response.data["error"]

def test_attendee_list_pagination(client, sample_event):
    for i in range(15):
        Attendee.objects.create(name=f"User{i}", email=f"user{i}@test.com", event=sample_event)

    url = reverse('list_attendees', args=[sample_event.id])
    response = client.get(url)
    assert response.status_code == 200
    assert "results" in response.data
    assert len(response.data["results"]) == 10  
