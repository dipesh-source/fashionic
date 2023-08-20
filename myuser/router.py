"""Router for a calling an API."""
from . import viewset
from rest_framework import routers

router = routers.DefaultRouter()


router.register(
    "appointment", viewset.AppointmentViewset, basename="appointment"
)  # noqa: E501
router.register("staff", viewset.StaffViewset, basename="staff")

router.register("service", viewset.ServiceViewset, basename="service")

router.register("gallery", viewset.GalleryViewset, basename="gallery")

router.register("product", viewset.ProductViewset, basename="product")

router.register("purchase", viewset.PurchaseViewset, basename="purchase")

router.register("feedback", viewset.FeedbackViewset, basename="feedback")

router.register(
    "attendance", viewset.AppointmentViewset, basename="attendance"
)  # noqa: E501
