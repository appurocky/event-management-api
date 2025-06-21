from django.urls import path
from .views import (
    EventCreateView, EventListView, RegisterAttendeeView, EventAttendeesListView
)

urlpatterns = [
    path('events', EventCreateView.as_view(), name='create_event'),
    path('events/', EventListView.as_view(), name='list_events'),
    path('events/<int:event_id>/register', RegisterAttendeeView.as_view(), name='register_attendee'),
    path('events/<int:event_id>/attendees', EventAttendeesListView.as_view(), name='list_attendees'),
]
