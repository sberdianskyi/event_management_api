from django.urls import path, include
from rest_framework import routers

from event_management.views import EventViewSet


app_name = "event_management"

router = routers.DefaultRouter()
router.register("events", EventViewSet)

urlpatterns = [path("", include(router.urls))]
