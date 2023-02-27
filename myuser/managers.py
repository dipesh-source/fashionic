import datetime

from django.db import models
from django.db.models import Q
from datetime import timedelta


class AppointmentManager(models.Manager):
    """
    this manager will help to filterout the data from client request
    """

    def get_queryset(self):
        return super().get_queryset().all()

    def get_all_user_appointment(self, user):
        return super().get_queryset().filter(user=user)

    # this query will return all the data of the logged in user
    def get_current_appointment(self, user, name, phone):
        return super().get_queryset().filter(Q(user=user) & Q(name=name) | Q(phone))

    # this query will return all the today appointment
    def today_appointment(self, user):
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(app_date=datetime.date.today()))
        )

    # this query will return the tomorrow appointment dtata
    def tomorrow_appointment(self, user):
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(app_date__gt=datetime.date.today()))
        )

    # will get all the appointment for a any future time
    def after_hours(self, user, which):
        now = datetime.datetime.now()
        after = timedelta(hours=which)
        return (
            super()
            .get_queryset()
            .filter(
                Q(user=user)
                & Q(app_date=datetime.date.today())
                & Q(app_time__range=(now, now + after))
            )
        )

    # will get all the appointment of the afete next 1 hour
    def after_one_hours(self, user):
        now = datetime.datetime.now()
        after = timedelta(hours=1)
        return (
            super()
            .get_queryset()
            .filter(
                Q(user=user)
                & Q(app_date=datetime.date.today())
                & Q(app_time__range=(now, now + after))
            )
        )


class ServiceManager(models.Manager):
    """
    manager for the service models
    """

    def get_service(self, user):
        return super().get_queryset().filter(user=user)

    def search_service(self, user, name):
        return super().get_queryset().filter(user=user, name=name)


class StaffManager(models.Manager):
    """
    will manage the staff query as a custome model manager
    """

    def get_staff(self, user):
        return super().get_queryset().filter(user=user)

    def get_staff_limit(self, user):
        return super().get_queryset().filter(user=user).order_by("id").reverse()[:5]

    def search_staff(self, user, name, surname, phone, email, service):
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
    """
    will handle the feedback custome manager
    """

    def get_feedback(user):
        return super().get_queryset().filter(user=user)

    def search_feedbback(user, name, phone, feedback):
        return (
            super()
            .get_queryset()
            .filter(
                Q(user=user) | Q(name=name) | Q(phone=phone) | Q(feedback__in=feedback)
            )
        )


class ProductManager(models.Manager):
    """
    custome product manager to handel all the Query from backend
    """

    def get_product(self, user):
        return super().get_queryset().filter(user=user).order_by("id").reverse()[:7]

    def search_product(self, user, name, price, stock, note):
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
    """
    will render all the reqired customer purchases data to user
    """

    def get_purchase(user):
        return super().get_queryset().filter(user=user)

    def search_purchase(user, product, qty):
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(product=product) | Q(qty=qty))
        )

    def search_who(user, name, phone):
        return (
            super().get_queryset().filter(Q(user=user) & Q(name=name) | Q(phone=phone))
        )


class GalleryManager(models.Manager):
    """
    custome gallery model manager
    """

    def get_gallery(user):
        return super().get_queryset().filter(user=user)

    def search_gallery(user, name, about):
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(name=name) | Q(about__in=about))
        )


class AttendanceManager(models.Manager):
    """
    for a attedance queryset
    """

    def get_attedance(user):
        return super().get_queryset().filter(user=user)

    def search_in_attedance(user, in_date, in_time):
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(in_date=in_date) | Q(in_time=in_time))
        )

    def search_out_attedance(user, out_date, out_time):
        return (
            super()
            .get_queryset()
            .filter(Q(user=user) & Q(out_date=out_date) | Q(out_time=out_time))
        )
