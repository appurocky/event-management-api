from django.core.exceptions import ValidationError
from .models import Event, Attendee

def register_attendee(event_id, name, email):
    event = Event.objects.get(id=event_id)
    if event.attendees.count() >= event.max_capacity:
        raise ValidationError("Event is full.")

    if Attendee.objects.filter(event=event, email=email).exists():
        raise ValidationError("You are already registered.")

    return Attendee.objects.create(name=name, email=email, event=event)
