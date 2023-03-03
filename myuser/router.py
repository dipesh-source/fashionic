"""Router for a calling an API."""
from . import viewset
from rest_framework import routers

router = routers.DefaultRouter()


router.register("app", viewset.AppointmentViewset, basename="appointment")
router.register("staff", viewset.StaffViewset, basename="staff")
