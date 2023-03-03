"""Serializer of models to convert nativdata type to JSON."""
from rest_framework import serializers
from account.models import CustomUser


class UserRegistrationSerializer(serializers.ModelSerializer):
    """New user registration serializer."""

    email = serializers.EmailField(max_length=20)
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)  # noqa: E501

    class Meta:
        """Meta class."""

        model = CustomUser
        fields = ["email", "username", "phone", "password", "password2"]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, attrs):
        """Validate function."""
        password1 = attrs.get("password")
        password2 = attrs.get("password2")
        if password1 != password2:
            raise serializers.ValidationError(
                "Password & confirm password does not match"
            )
        return attrs

    def create(self, validated_data):
        """Will create a user while calling serializer."""
        return CustomUser.objects._create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    """Login for the authenticated user."""

    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        """Meta class for a LoginSerializer."""

        model = CustomUser
        fields = ["email", "password"]


class UserProfileSerializer(serializers.ModelSerializer):
    """Get current user for the display info."""

    service = serializers.StringRelatedField(many=True, read_only=True)
    staff = serializers.StringRelatedField(many=True, read_only=True)
    appointment = serializers.StringRelatedField(many=True, read_only=True)
    feedback = serializers.StringRelatedField(many=True, read_only=True)
    product = serializers.StringRelatedField(many=True, read_only=True)
    purchase = serializers.StringRelatedField(many=True, read_only=True)
    gallery = serializers.StringRelatedField(many=True, read_only=True)
    attendance = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        """Meta class for a UserProfileSerializer."""

        model = CustomUser
        fields = [
            "email",
            "username",
            "service",
            "staff",
            "appointment",
            "feedback",
            "product",
            "purchase",
            "gallery",
            "attendance",
        ]


class ChangeUSerPassword(serializers.Serializer):
    """Authenticated user will change their old password to new password."""

    password = serializers.CharField(
        max_length=20, style={"input_type": "password"}, write_only=True
    )
    password2 = serializers.CharField(
        max_length=20, style={"input_type": "password"}, write_only=True
    )

    class Meta:
        """Meta class for a ChangeUSerPassword."""

        fields = ["password", "password2"]

    def validate(self, data):
        """Validate function for a password."""
        password1 = data.get("password")
        password2 = data.get("password2")
        user = self.context.get("user")
        if password1 != password2:
            raise serializers.ValidationError("password does not match")
        user.set_password(password1)
        user.save()
        return data
