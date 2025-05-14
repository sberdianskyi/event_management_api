from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import AllowAny
from rest_framework.settings import api_settings

from user.serializers import UserSerializer


@extend_schema_view(
    create=extend_schema(
        summary="Create new user",
        description="Register a new user in the system",
        responses={
            status.HTTP_201_CREATED: {"description": "User successfully created"},
            status.HTTP_400_BAD_REQUEST: {
                "description": "Invalid input data",
                "example": {
                    "username": ["This field is required."],
                    "password": ["This field is required."],
                },
            },
        },
    )
)
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


@extend_schema_view(
    post=extend_schema(
        summary="Create auth token",
        description="Obtain authentication token for user login",
        responses={
            status.HTTP_200_OK: {
                "description": "Login successful",
                "example": {"token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"},
            },
            status.HTTP_400_BAD_REQUEST: {
                "description": "Invalid credentials",
                "example": {
                    "non_field_errors": ["Unable to log in with provided credentials."]
                },
            },
        },
    )
)
class LoginUserView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
