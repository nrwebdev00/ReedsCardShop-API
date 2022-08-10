from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import (
    UserSerializer,
    CollectorSerializer,
    SellerSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):

    serializer_class = UserSerializer


class CreateCollectorView(generics.CreateAPIView):

    serializer_class = CollectorSerializer


class CreateSellerView(generics.CreateAPIView):

    serializer_class = SellerSerializer


class CreateTokenView(ObtainAuthToken):

    serializer_class = AuthTokenSerializer
    renderer_class = api_settings.DEFAULT_RENDERER_CLASSES
