from rest_framework import serializers


from event_management.models import Event, EventRegistration


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = ("id", "title", "description", "date", "location", "organizer")


class EventListSerializer(EventSerializer):
    registrations_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "description",
            "date",
            "location",
            "organizer",
            "registrations_count",
        )

    def get_registrations_count(self, obj):
        return obj.registrations.count()


class EventRegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventRegistration
        fields = (
            "id",
            "event",
            "registration_date",
        )


class EventRegistrationListSerializer(EventRegistrationSerializer):
    event = serializers.SlugRelatedField(many=False, read_only=True, slug_field="title")


class EventRegistrationDetailSerializer(EventRegistrationSerializer):
    event = EventSerializer(many=False, read_only=True)
