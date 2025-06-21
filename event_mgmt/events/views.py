from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils.timezone import now
from .models import Event, Attendee
from .serializers import EventSerializer, AttendeeSerializer
from .services import register_attendee

class EventCreateView(generics.CreateAPIView):
    serializer_class = EventSerializer

class EventListView(generics.ListAPIView):
    serializer_class = EventSerializer

    def get_queryset(self):
        return Event.objects.filter(start_time__gte=now()).order_by('start_time')

class RegisterAttendeeView(APIView):
    def post(self, request, event_id):
        try:
            attendee = register_attendee(
                event_id,
                name=request.data.get('name'),
                email=request.data.get('email')
            )
            return Response(AttendeeSerializer(attendee).data, status=201)
        except Exception as e:
            return Response({"error": str(e)}, status=400)

class EventAttendeesListView(generics.ListAPIView):
    serializer_class = AttendeeSerializer

    def get_queryset(self):
        event_id = self.kwargs['event_id']
        return Attendee.objects.filter(event__id=event_id)


