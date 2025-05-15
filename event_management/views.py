from django.db import IntegrityError
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from event_management.models import Event, EventRegistration
from event_management.serializers import (
    EventSerializer,
    EventRegistrationSerializer,
    EventRegistrationListSerializer,
    EventRegistrationDetailSerializer,
    EventListSerializer,
)


@extend_schema_view(
    list=extend_schema(
        summary="Get list of events",
        description="Returns list of all available events with registration count",
    ),
    retrieve=extend_schema(
        summary="Get event details",
        description="Returns detailed information about specific event",
    ),
    create=extend_schema(summary="Create event", description="Creates a new event"),
    update=extend_schema(summary="Update event", description="Updates existing event"),
    destroy=extend_schema(summary="Delete event", description="Deletes existing event"),
)
class EventViewSet(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return EventListSerializer
        return EventSerializer


@extend_schema_view(
    list=extend_schema(
        summary="Get list of registrations",
        description="Returns list of current user's event registrations",
    ),
    retrieve=extend_schema(
        summary="Get registration details",
        description="Returns detailed information about specific registration",
    ),
    create=extend_schema(
        summary="Register for event",
        description="Creates new event registration",
        responses={
            400: {
                "description": "Duplicate registration error",
                "example": {"detail": "You are already registered for this event."},
            }
        },
    ),
    destroy=extend_schema(
        summary="Cancel registration", description="Deletes existing registration"
    ),
)
class EventRegistrationViewSet(
    GenericViewSet,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
):

    queryset = EventRegistration.objects.all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return EventRegistration.objects.filter(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return EventRegistrationListSerializer
        if self.action == "retrieve":
            return EventRegistrationDetailSerializer
        return EventRegistrationSerializer

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError(
                {"detail": "You are already registered for this event."}
            )
