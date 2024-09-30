from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'bio', 'profile_picture')
        # Ensure password is write-only
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Use create_user to ensure the password is hashed
        user = get_user_model().objects.create_user(**validated_data)
        # Create a token for the new user
        token, _ = Token.objects.get_or_create(user=user)
        return {
            'user_id': user.id,
            'token': token.key
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        # Perform custom validation for login
        user = authenticate(
            username=attrs['username'], password=attrs['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")

        # Create or get token for the authenticated user
        token, _ = Token.objects.get_or_create(user=user)
        attrs['user'] = user
        # Add token to the validated attrs for response
        attrs['token'] = token.key

        return attrs
