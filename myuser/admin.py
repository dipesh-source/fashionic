"""Admin file to register a model."""
from django.contrib import admin
from .models import (
    Service,
    Staff,
    Appointment,
    Feedback,
    Product,
    Purchase,
    Gallery,
    Attendance,
)


@admin.register(Appointment)
class appointmentAdmin(admin.ModelAdmin):
    """Register a appointmentAdmin."""

    list_display = [
        "id",
        "user",
        "name",
        "surname",
        "phone",
        "app_date",
        "app_time",
        "provided",
    ]
    list_display = (
        "user",
        "name",
        "surname",
        "phone",
        "app_date",
        "app_time",
        "provided",
    )
    list_filter = (
        "user",
        "name",
        "surname",
        "phone",
        "app_date",
        "app_time",
        "provided",
    )
    search_fields = ["name", "surname", "phone"]


@admin.register(Service)
class serviceAdmin(admin.ModelAdmin):
    """Register a serviceAdmin."""

    list_display = [
        "id",
        "user",
        "img",
        "name",
        "cost",
        "text",
    ]


@admin.register(Feedback)
class feedbackAdmin(admin.ModelAdmin):
    """Register a feedbackAdmin."""

    list_display = [
        "id",
        "user",
        "name",
        "phone",
        "feedback",
    ]


@admin.register(Gallery)
class galleryAdmin(admin.ModelAdmin):
    """Register a galleryAdmin."""

    list_display = [
        "id",
        "name",
        "img",
        "file",
        "about",
    ]


@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    """Register a productAdmin."""

    list_display = [
        "id",
        "user",
        "img",
        "name",
        "price",
        "stock",
        "note",
    ]


@admin.register(Staff)
class staffAdmin(admin.ModelAdmin):
    """Register a staffAdmin."""

    list_display = [
        "id",
        "profile",
        "name",
        "surname",
        "phone",
        "email",
        "specialization",
    ]


@admin.register(Purchase)
class purchaseAdmin(admin.ModelAdmin):
    """Register a purchaseAdmin."""

    list_display = [
        "id",
        "user",
        "product",
        "name",
        "phone",
        "qty",
    ]


@admin.register(Attendance)
class attedanceaAdmin(admin.ModelAdmin):
    """Register a attedanceaAdmin."""

    list_display = ["id", "staff", "date", "is_present"]
