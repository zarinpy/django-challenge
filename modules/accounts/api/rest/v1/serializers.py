from django.contrib.auth.models import update_last_login
from django.db.utils import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.tokens import RefreshToken

from modules.domain.models import User


class SignUpSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=100, required=True, write_only=True)
    password = serializers.CharField(min_length=4, required=True, write_only=True)
    first_name = serializers.CharField(max_length=300, required=True)
    last_name = serializers.CharField(max_length=300, required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                username=validated_data['username'],
                first_name=validated_data['first_name'],
                last_name=validated_data['last_name']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
        except IntegrityError:
            raise ValidationError("user with this username exist.")


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100, required=True, write_only=True)
    password = serializers.CharField(min_length=4, required=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        try:
            user = User.objects.get(username=username)
            if user.check_password(validated_data['password']):
                refresh = RefreshToken.for_user(user)
                access = str(refresh.access_token)

                if api_settings.UPDATE_LAST_LOGIN:
                    update_last_login(None, user)

                return {
                    'access': access,
                    'refresh': str(refresh)
                }
            else:
                raise serializers.ValidationError('Password or username incorrect')
        except User.DoesNotExist:
            raise serializers.ValidationError('Password or username incorrect')
