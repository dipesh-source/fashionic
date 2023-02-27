"""
    authentication viewset business logic
"""
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from . import serializers


def get_tokens_for_user(user):
    """while generate token function will call"""
    refresh = RefreshToken.for_user(user)

    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class RegistrationViewSet(views.APIView):
    """user will register his new account"""

    def post(self, request):
        """function for the user"""
        serializer = serializers.UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            return Response(
                {"token": token, "data": "user registered"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)


class LoginViewSet(views.APIView):
    """
    user will login his/her account
    """

    authentication_classes = [JWTAuthentication]

    def get(self, request):
        """access GET method to implement logic"""
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get("email")
            password = serializer.data.get("password")
            print("username ", email, "password", password)
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({"token": token, "data": "Logged in success"})
            return Response(
                {"errors": {"non_field_errors": ["Email or password not a valid"]}},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfile(views.APIView):
    """
    user profile come from here
    """

    authentication_classes = [JWTAuthentication]

    def get(self, request):
        serializer = serializers.UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
