from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    organizer = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class EventRegistration(models.Model):
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="registrations"
    )
    user = models.ForeignKey(
        "user.User", on_delete=models.CASCADE, related_name="event_registrations"
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["event", "user"], name="unique_event_registration"
            )
        ]
