from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from apps.auths.services import login_register, verify_login_register
from apps.utilities.messages import CommonMessages
from apps.utilities.serializers import ErrorSerializer


class LoginRegisterApiView(APIView):
    class LoginRegisterInputSerializer(serializers.Serializer):
        email = serializers.EmailField(allow_blank=True)
        phone_number = serializers.CharField(allow_blank=True)
        isd = serializers.CharField(allow_blank=True)

    class LoginRegisterOutputSerializer(serializers.Serializer):
        uuid_token = serializers.UUIDField()

    @extend_schema(
        request=LoginRegisterInputSerializer,
        responses={
            200: LoginRegisterOutputSerializer,
            400: ErrorSerializer,
        },
    )
    def post(self, request):
        serializer = self.LoginRegisterInputSerializer(data=request.data)
        if serializer.is_valid():
            result, status = login_register(data=serializer.data)
            return Response(result, status)
        return Response(
            CommonMessages.data_not_valid.value[0],
            status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
        )


class VerifyLoginRegisterApiView(APIView):
    class VerifyLoginRegisterInputSerializer(serializers.Serializer):
        uuid_token = serializers.UUIDField()
        password = serializers.CharField(max_length=6)

    class VerifyLoginRegisterOutputSerializer(serializers.Serializer):
        refresh = serializers.CharField()
        access = serializers.CharField()

    @extend_schema(
        request=VerifyLoginRegisterInputSerializer,
        responses={200: VerifyLoginRegisterOutputSerializer, 400: ErrorSerializer},
    )
    def post(self, request):
        serializer = self.VerifyLoginRegisterInputSerializer(data=request.data)
        if serializer.is_valid():
            result, status_code = verify_login_register(data=serializer.data)
            return Response(result, status_code)
        return Response(
            CommonMessages.data_not_valid.value[0],
            status=status.HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS,
        )
