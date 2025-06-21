from rest_framework import serializers
from .models import Event, Attendee

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
    
    def update(self, instance, validated_data):
        old_tz = pytz.timezone(instance.timezone)
        new_tz_name = validated_data.get("timezone", instance.timezone)
        new_tz = pytz.timezone(new_tz_name)

        if new_tz_name != instance.timezone:
            start = instance.start_time.astimezone(old_tz)
            end = instance.end_time.astimezone(old_tz)
            instance.start_time = new_tz.localize(start.replace(tzinfo=None)).astimezone(pytz.UTC)
            instance.end_time = new_tz.localize(end.replace(tzinfo=None)).astimezone(pytz.UTC)

        instance.timezone = new_tz_name
        return super().update(instance, validated_data)
    
class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendee
        fields = ['id', 'name', 'email', 'event']
        read_only_fields = ['event']
