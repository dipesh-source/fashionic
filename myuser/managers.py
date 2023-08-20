"""Custom model managers."""
import datetime

from django.db import models
from django.db.models import Q
from datetime import timedelta, date


class AppointmentManager(models.Manager):
    """this manager will help to filter out the data from client request."""

    def get_queryset(self):
        """Return get queryset."""
        return super().get_queryset().all()

    def get_all_user_appointment(self, user):
        """Get all user appointment."""
        return super().get_queryset().filter(user=user)

    def get_current_appointment(self, user, name, phone):
        """Get appointment by username and phone number & query will return all the data of the logged in user."""  # noqa: E501
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(name=name) | Q(phone))  # noqa: E501
        )

    def today_appointment(self, user):
        """Get today appointment."""
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(app_date=datetime.date.today()))
        )

    # this query will return the tomorrow appointment data
    def tomorrow_appointment(self, user):
        """Get all tomorrow appointment."""
        tomorrow = date.today() + timedelta(days=1)
        return (
            super().get_queryset().filter(Q(user=user) & Q(app_date=tomorrow))
        )  # noqa: E501

    def after_hours(self, user, which):
        """Get any future hour appointment or get after 1 hour."""
        now = datetime.datetime.now()
        if which is not None:
            after = timedelta(hours=int(which))
            hour = now + after
        else:
            next = timedelta(hours=1)
            time_formatted = now + next
            hour = time_formatted.strftime("%H:%M:%S")  # Format as HH:MM:SS
        return (
            super()
            .get_queryset()
            .filter(
                Q(user=user)
                & Q(app_date=datetime.date.today())
                & Q(app_time__range=(now, hour))
            )
        )


class ServiceManager(models.Manager):
    """Manager for the service models."""

    def get_service(self, user):
        """Get queryset."""
        return super().get_queryset().filter(user=user)

    def search_service(self, user, name):
        """Search services."""
        return super().get_queryset().filter(user=user, name=name)


class StaffManager(models.Manager):
    """Will manage the staff query as a custom model manager."""

    def get_staff(self, user):
        """Get all logged in staff data."""
        return super().get_queryset().filter(user=user)

    # TODO: replace with Django search.
    def search_staff(self, user, name, surname, phone, email, service):
        """Search staff by all data."""
        return (
            super()
            .get_queryset()
            .filter(
                Q(user=user) & Q(name=name)
                | Q(surname=surname)
                | Q(phone=phone)
                | Q(email=email)
                | Q(Service=service)
            )
        )


class FeedbackManager(models.Manager):
    """Will handle the feedback custom manager."""

    def get_feedback(self, user):
        """Get all logged in feedback."""
        return super().get_queryset().filter(user=user)

    # TODO: replace with Django search.
    def search_feedback(self, user, name, phone, feedback):
        """Search feedback."""
        return (
            super()
            .get_queryset()
            .filter(
                Q(user=user)
                | Q(name=name)
                | Q(phone=phone)
                | Q(feedback__in=feedback)  # noqa: E501
            )
        )


class ProductManager(models.Manager):
    """Custom product manager to handel all the Query from backend."""

    def get_product(self, user):
        """Get products."""
        return (
            super()
            .get_queryset()
            .filter(user=user)
            .order_by("id")
            .reverse()  # noqa: E501
        )

    # TODO: replace with django backend search.
    def search_product(self, user, name, price, stock, note):
        """Search all product."""
        return (
            super()
            .get_queryset()
            .filter(
                Q(user=user) & Q(name=name)
                | Q(price=price)
                | Q(stock=stock)
                | Q(note=note)
            )
        )


class PurchaseManager(models.Manager):
    """Will render all the required customer purchases data to user."""

    def get_purchase(self, user):
        """Get all purchase of logged in users."""
        return super().get_queryset().filter(user=user)

    # TODO: replace with django backend search.
    def search_purchase(self, user, product, qty):
        """Search any purchase."""
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(product=product) | Q(qty=qty))
        )

    def search_who(self, user, name, phone):
        """Search purchased user."""
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(name=name) | Q(phone=phone))  # noqa: E501
        )


class GalleryManager(models.Manager):
    """Custom gallery model manager."""

    def get_gallery(self, user):
        """Get all logged in user gallery."""
        return super().get_queryset().filter(user=user)

    # TODO: replace with django backend search.
    def search_gallery(self, user, name, about):
        """Search galley items."""
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(name=name) | Q(about__in=about))
        )


class AttendanceManager(models.Manager):
    """For a attendance queryset."""

    def get_attendance(self, user):
        """Get all logged in user attendance."""
        return super().get_queryset().filter(user=user)

    # TODO: replace with django backend search.
    def search_in_attendance(self, user, in_date, in_time):
        """Search in attendance."""
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(in_date=in_date) | Q(in_time=in_time))
        )

    # TODO: replace with django backend search.
    def search_out_attendance(self, user, out_date, out_time):
        """Search out attendance."""
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(out_date=out_date) | Q(out_time=out_time))
        )
