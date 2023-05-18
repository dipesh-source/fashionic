"""Generating fake data from faker library."""
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "fashionic.settings")

# Django
import django  # noqa: E402

django.setup()

# Faker
from faker import Faker  # noqa: E402
from django.conf import settings  # noqa: E402

# from django.utils import timezone  # noqa: E402
from django.core.management.base import BaseCommand  # noqa: E402

# App
from myuser.models import Appointment, Service, Staff  # noqa: E402


User = settings.AUTH_USER_MODEL


class Command(BaseCommand):
    """Common class."""

    help = "Generate fake appointments"

    def add_arguments(self, parser):
        """Add argument in tofunction."""
        parser.add_argument(
            "num_appointments",
            type=int,
            help="Number of appointments to generate",  # noqa: E501
        )

    def handle(self, *args, **kwargs):
        """Handle the function."""
        num_appointments = kwargs["num_appointments"]
        fake = Faker()

        # Query all services and staff from the database
        services = Service.objects.all()
        staff = Staff.objects.all()
        print("XXXXXXXXXX", services, staff)

        # Create a list of Appointment objects using Faker library
        appointments = [
            Appointment(
                user=User.objects.first(),  # replace this with your own logic
                name=fake.first_name(),
                surname=fake.last_name(),
                phone=fake.phone_number(),
                app_date=fake.date_between(
                    start_date="today", end_date="+30d"
                ),  # noqa: E501
                app_time=fake.time(),
                provided=staff[fake.random_int(min=0, max=staff.count() - 1)],
            )
            for _ in range(num_appointments)
        ]

        # Use bulk_create to save all appointments in a single query
        Appointment.objects.bulk_create(appointments)

        # Add services to each appointment using Faker library
        for appointment in Appointment.objects.all():
            appointment.service.set(
                services.order_by("?")[: fake.random_int(min=0, max=3)]
            )
