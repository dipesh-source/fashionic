"""Created a API for a models."""
from myuser.models import Staff, Appointment, Service
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from .serializers import (
    AppointmentSerializer,
    StaffSerializer,
    ServiceSerializer,
)  # noqa: E501
from account.models import CustomUser
from rest_framework.permissions import IsAuthenticated

User = CustomUser


class AppointmentViewset(viewsets.ModelViewSet):
    """AppointmentViewset API."""

    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Override appointment query."""
        user = self.request.user
        return Appointment.objectsAppointment.get_all_user_appointment(
            user
        )  # noqa: E501


class StaffViewset(viewsets.ModelViewSet):
    """StaffViewset API."""

    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self, request):
        """Get queryset for a StaffViewset."""
        return Staff.objectStaff.get_staff(user=request.user)


class ServiceViewset(viewsets.ModelViewSet):
    """Service api."""

    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
