from rest_framework import serializers


from event_management.models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    Serializer for the Event model.
    """

    class Meta:
        model = Event
        fields = ("id", "title", "description", "date", "location", "organizer")
