from django.urls import path, include
from rest_framework import routers

from event_management.views import EventViewSet, EventRegistrationViewSet


app_name = "event_management"

router = routers.DefaultRouter()
router.register("events", EventViewSet)
router.register("registrations", EventRegistrationViewSet)

urlpatterns = [path("", include(router.urls))]
