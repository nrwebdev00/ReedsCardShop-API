from rest_framework import generics
from user.serializers import (
    UserSerializer,
    CollectorSerializer,
    SellerSerializer
)


class CreateUserView(generics.CreateAPIView):

    serializer_class = UserSerializer


class CreateCollectorView(generics.CreateAPIView):

    serializer_class = CollectorSerializer


class CreateSellerView(generics.CreateAPIView):

    serializer_class = SellerSerializer
