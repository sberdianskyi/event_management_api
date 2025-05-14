from rest_framework import viewsets

from event_management.models import Event
from event_management.serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing event instances.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
