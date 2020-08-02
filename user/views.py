# Create your views here.

from django.contrib.auth import login
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response

from .models import Address
from .serializers import RegisterSerializer, AddressSerializer,GetAddressSerializer,ValidateAddressSerializer


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            return Response({
                "status": "OK",
                "statusCode": status.HTTP_200_OK,
                "message": "success",
                "user_data": {
                    'user_id': user.pk,
                    'email': user.email,
                    'username': user.username,
                    "token": AuthToken.objects.create(user)[1],
                },
            })
        else:
            return Response({
                "status": "ERROR",
                "statusCode": status.HTTP_400_BAD_REQUEST,
                "message": serializer.errors,
            })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        try:
            serializer = AuthTokenSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                user = serializer.validated_data['user']
                login(request, user)
                return Response({
                    "status": "OK",
                    "statusCode": status.HTTP_200_OK,
                    "message": "success",
                    "user_data": {
                        'user_id': user.pk,
                        'email': user.email,
                        'username': user.username,
                        "token": AuthToken.objects.create(user)[1],
                    },
                })
            else:
                return Response({
                    "status": "ERROR",
                    "statusCode": status.HTTP_400_BAD_REQUEST,
                    "message": serializer.errors,
                })

        except user.DoesNotExist:
            return Response({
                "status": "ERROR",
                "statusCode": status.HTTP_404_NOT_FOUND,
                "message": "User not found",
            })


class SaveAddressAPI(generics.GenericAPIView):
    serializer_class = AddressSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = AddressSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                address = serializer.save()
                return Response({
                    "status": "OK",
                    "statusCode": status.HTTP_200_OK,
                    "message": "Success",
                })
            else:
                return Response({
                    "status": "ERROR",
                    "statusCode": status.HTTP_400_BAD_REQUEST,
                    "message": serializer.errors,
                })
        except:
            return Response({
                "status": "ERROR",
                "statusCode": status.HTTP_400_BAD_REQUEST,
                "message": serializer.errors,
            })


class GetAddressAPI(generics.GenericAPIView):
    def post(self, request):

        try:
            serializer = ValidateAddressSerializer(data=request.data)

            model = Address.objects.filter(user_id=request.POST['user_id'])
            serializer = GetAddressSerializer(model, many=True)
            return Response({
                "status": "OK",
                "statusCode": status.HTTP_200_OK,
                "message": "Success",
                "address_list": serializer.data
            })
        except Address.DoesNotExist:
            return Response({
                "status": "ERROR",
                "statusCode": status.HTTP_404_NOT_FOUND,
                "message": "User not found",
            })
