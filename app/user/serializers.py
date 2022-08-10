from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext as _
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}


    def create_user(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class CollectorSerializer(serializers.ModelSerializer):


    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name', 'is_collector')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

    def create_collector(self, validated_data):
        return get_user_model().objects.create_user_collector(**validated_data)


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name', 'is_collector', 'is_seller')
        extra_kwargs = {'password': {'write_only': True, 'min_length':8}}

    def create_seller(self, validated_data):
        return get_user_model().objects.create_user_seller(**validated_data)


class AuthTokenSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):

        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


