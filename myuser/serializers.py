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


class AppointmentDaySerializer(serializers.ModelSerializer):
    """Get today, tomorrow and specific day serializer."""

    # TODO: might we can use common AppointmentSerializer for both.
    service = serializers.StringRelatedField(many=True, read_only=True)
    provided = serializers.StringRelatedField(read_only=True)

    class Meta:
        """Meta django class."""

        model = Appointment
        fields = [
            "id",
            "user",
            "name",
            "surname",
            "phone",
            "app_date",
            "app_time",
            "service",
            "provided",
        ]


class AppointmentSerializer(serializers.ModelSerializer):
    """Create a serializer for the save appointment."""

    service = serializers.StringRelatedField(many=True, read_only=True)
    provided = serializers.PrimaryKeyRelatedField(
        queryset=Staff.objects.none(), required=True
    )

    def __init__(self, *args, **kwargs):
        """Handle to get current object of staff."""
        super().__init__(*args, **kwargs)
        self.fields["provided"].queryset = Staff.objects.filter(
            user=self.context["request"].user
        )
        print(self.context["request"])
        print(self.context["request"].user)

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
            "service",
            "provided",
        ]


class StaffSerializer(serializers.ModelSerializer):
    """Create a staff modelserializer."""

    app_staff = serializers.StringRelatedField(many=True, read_only=True)
    staff_attendance = serializers.StringRelatedField(
        many=True, read_only=True
    )  # noqa: E501

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
            "app_staff",
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
        fields = [
            "id",
            "user",
            "img",
            "name",
            "price",
            "stock",
            "note",
            "product",
        ]  # noqa: E501


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
