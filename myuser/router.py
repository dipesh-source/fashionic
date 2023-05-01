"""Router for a calling an API."""
from . import viewset
from rest_framework import routers

router = routers.DefaultRouter()


router.register(
    "appointment", viewset.AppointmentViewset, basename="appointment"
)  # noqa: E501
router.register("staff", viewset.StaffViewset, basename="staff")

router.register("service", viewset.ServiceViewset, basename="service")
