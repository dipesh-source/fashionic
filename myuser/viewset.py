"""Created a API for a models."""

# Rest framework
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework_simplejwt.authentication import JWTAuthentication

# App
from .serializers import (
    AppointmentSerializer,
    StaffSerializer,
    ServiceSerializer,
    AppointmentDaySerializer,
    FeedbackSerializer,
    ProductSerializer,
    PurchaseSerializer,
)  # noqa: E501
from account.models import CustomUser
from myuser.models import (
    Staff,
    Appointment,
    Service,
    Feedback,
    Product,
    Purchase,
)  # noqa: E501

# Django
# from django_filters.rest_framework import DjangoFilterBackend

User = CustomUser


class AppointmentViewset(viewsets.ModelViewSet):
    """AppointmentViewset API."""

    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = (
        SearchFilter,
        OrderingFilter,
        # DjangoFilterBackend,
    )

    def get_queryset(self):
        """Override appointment query."""
        user = self.request.user
        return Appointment.objectsAppointment.get_all_user_appointment(
            user
        )  # noqa: E501

    def create(self, request, *args, **kwargs):
        """Override create method."""
        serializer = AppointmentSerializer(
            data=request.data, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            services = request.data.get(
                "service", []
            )  # get the list of services from the request data
            appointment = serializer.save()
            appointment.service.set(services)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": "something went wrong"},
            status=status.HTTP_400_BAD_REQUEST,  # noqa: E501
        )

    @action(detail=False, methods=["GET"])
    def days_appointment(self, request, pk=None):
        """Return all today appointment data."""
        user = self.request.user
        data = request.query_params.get("day", None)
        if data == "today":
            queryset = Appointment.objectsAppointment.today_appointment(
                user
            )  # noqa: E501
            if not queryset.exists():
                return Response(
                    {"Error": "Today appointment not found"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer = AppointmentDaySerializer(queryset, many=True)
        elif data == "tomorrow":
            queryset = Appointment.objectsAppointment.tomorrow_appointment(
                user
            )  # noqa: E501
            if not queryset.exists():
                return Response(
                    {"Error": "Tomorrow appointment not found"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer = AppointmentDaySerializer(queryset, many=True)
        return Response(
            {"today-appointment": serializer.data},
            status=status.HTTP_200_OK,  # noqa: E501
        )

    @action(detail=False, methods=["GET"])
    def hours(self, request):
        """Handle future hour and after next 1 hour appointment."""
        user = self.request.user
        params = request.query_params.get("hour", None)
        queryset = Appointment.objectsAppointment.after_hours(user, params)
        if not queryset.exists():
            return Response(
                {"Error": "Hour's appointment not found"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = AppointmentSerializer(
            queryset, many=True, context={"request": request}
        )
        return Response(
            {"hours-appointment": serializer.data},
            status=status.HTTP_200_OK,  # noqa: E501
        )


class StaffViewset(viewsets.ModelViewSet):
    """StaffViewset API."""

    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Get queryset for a StaffViewset."""
        user = self.request.user
        return Staff.objectStaff.get_staff(user)


class ServiceViewset(viewsets.ModelViewSet):
    """Service api."""

    serializer_class = ServiceSerializer
    queryset = Service.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Queryset for services API."""
        user = self.request.user
        return Service.objectsService.get_service(user)

    @action(detail=False, methods=["GET"])
    def search_services(self, request, pk=None):
        """Add query params for search services."""
        user = self.request.user
        # TODO: I have to learn self.get_queryset
        testing = self.get_queryset()
        print("Base Queryset from Testing", testing)
        data = request.query_params.get("services", None)
        if data is None:
            return Response(
                {"Error": "Searched data not found"},
                status=status.HTTP_400_BAD_REQUEST,  # noqa: E501
            )
        new_query = self.get_serializer()
        test = self.get_serializer_class()
        print("Get serializer class", new_query, test)
        query = Service.objectsService.search_service(user, data)
        serializer = ServiceSerializer(query, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)


class FeedbackViewset(viewsets.ModelViewSet):
    """Feedback api of all users."""

    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Override queryset to get logged in user."""
        user = self.request.user
        return Feedback.objectsFeedback.get_feedback(user)


class ProductViewset(viewsets.ModelViewSet):
    """Product API viewset."""

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        """Override the queryset for product."""
        user = self.request.user
        return Product.objectsProduct.get_product(user)


class PurchaseViewset(viewsets.ModelViewSet):
    """Purchase API viewset."""

    serializer_class = PurchaseSerializer
    queryset = Purchase.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Override the get_queryset."""
        user = self.request.user
        return Purchase.objectsPurchase.get_purchase(user)
