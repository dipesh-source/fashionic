"""Created a API for a models."""
from myuser.models import Staff, Appointment
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from .serializers import AppointmentSerializer, StaffSerializer
from account.models import CustomUser
from rest_framework.permissions import IsAuthenticated

User = CustomUser


class AppointmentViewset(viewsets.ModelViewSet):
    """AppointmentViewset API."""

    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


class StaffViewset(viewsets.ModelViewSet):
    """StaffViewset API."""

    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self, request):
        """Get queryset for a StaffViewset."""
        return Staff.objectStaff.get_staff(user=request.user)
