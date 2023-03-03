"""Serializer file for convert into a Json."""
from rest_framework import serializers
from myuser.models import (
    Service,
    Staff,
    Appointment,
    Feedback,
    Product,
    Purchase,
    Gallery,
    Attendance,
)


class AppointmentSerializer(serializers.ModelSerializer):
    """Create a serializer for the save appointment."""

    app_service = serializers.StringRelatedField(many=True, read_only=True)
    app_staff = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        """Nested class."""

        model = Appointment
        fields = [
            "id",
            "user",
            "name",
            "surname",
            "phone",
            "app_date",
            "app_time",
            "app_service",
            "app_staff",
        ]


class StaffSerializer(serializers.ModelSerializer):
    """Create a staff modelserializer."""

    staff_attendance = serializers.StringRelatedField(many=True, read_only=True)  # noqa: E501

    class Meta:
        """Nested class."""

        model = Staff
        fields = [
            "id",
            "user",
            "profile",
            "name",
            "surname",
            "phone",
            "email",
            "specialization",
            "staff_attendance",
        ]


class ServiceSerializer(serializers.ModelSerializer):
    """Service model serializers."""

    class Meta:
        """Nested class."""

        model = Service
        fields = ["id", "user", "name", "cost", "text"]


class AttendanceSerializer(serializers.ModelSerializer):
    """Have a attendance serializers."""

    class Meta:
        """Nested class."""

        model = Attendance
        fileds = [
            "id",
            "user",
            "staff",
            "date",
            "is_present",
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    """Feedback modelserializers."""

    class Meta:
        """Nested class."""

        model = Feedback
        fields = ["id", "user", "name", "phone", "feedback"]


class ProductSerializer(serializers.ModelSerializer):
    """Create a product serializers."""

    product = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        """Nested class."""

        model = Product
        fields = ["id", "user", "img", "name", "price", "stock", "note"]


class PurchaseSerializer(serializers.ModelSerializer):
    """Create a purchase modelserializer."""

    product = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        """Nested class."""

        model = Purchase
        fields = ["id", "user", "product", "name", "phone", "qty", "product"]


class GallerySerializer(serializers.ModelSerializer):
    """GallerySerializer."""

    class Meta:
        """Nested class."""

        model = Gallery
        fields = ["id", "user", "name", "img", "file", "about"]
