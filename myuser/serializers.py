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
    """
    create a serializer for the save appointment
    """

    app_service = serializers.StringRelatedField(many=True, read_only=True)
    app_staff = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
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

    # def create(self, validated_data):
    #     validated_data['user'] = self.context['request'].user
    #     return Appointment.objects.create(**validated_data)


class StaffSerializer(serializers.ModelSerializer):
    """
    create a staff modelserializer
    """

    staff_attendance = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
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
    """
    service model serializers
    """

    class Meta:
        model = Service
        fields = ["id", "user", "name", "cost", "text"]


class ProductSerializer(serializers.ModelSerializer):
    """
    product model serializer
    """

    class Meta:
        model = ["id", "user", "img", "name", "price", "stock", "note"]


class AttendanceSerializer(serializers.ModelSerializer):
    """
    have a attendance serializers
    """

    class Meta:
        model = Attendance
        fileds = [
            "id",
            "user",
            "staff",
            "date",
            "is_present",
        ]


class FeedbackSerializer(serializers.ModelSerializer):
    """
    feedback modelserializers
    """

    class Meta:
        model = Feedback
        fields = ["id", "user", "name", "phone", "feedback"]


class ProductSerializer(serializers.ModelSerializer):
    """
    create a product serializers
    """

    class Meta:
        model = Product
        fields = ["id", "user", "img", "name", "price", "stock", "note"]


class PurchaseSerializer(serializers.ModelSerializer):
    """
    create a purchase modelserializer
    """

    product = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Purchase
        fields = ["id", "user", "product", "name", "phone", "qty", "product"]


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ["id", "user", "name", "img", "file", "about"]
