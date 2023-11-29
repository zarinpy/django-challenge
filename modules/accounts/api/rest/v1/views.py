from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from modules.accounts.api.rest.v1.serializers import (LoginSerializer,
                                                      SignUpSerializer)
from modules.domain.models import User


class SignUpView(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [AllowAny]


class LoginView(GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    @extend_schema(request=LoginSerializer)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(result, status=status.HTTP_200_OK, headers=headers)
