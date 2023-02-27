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


@admin.register(Service)
class serviceAdmin(admin.ModelAdmin):
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
    list_display = [
        "id",
        "user",
        "name",
        "phone",
        "feedback",
    ]


@admin.register(Gallery)
class galleryAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "img",
        "file",
        "about",
    ]


@admin.register(Product)
class productAdmin(admin.ModelAdmin):
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
    list_display = [
        "id",
        "in_date",
        "in_time",
        "out_date",
        "out_time",
        "check_out",
    ]
