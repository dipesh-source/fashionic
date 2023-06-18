"""Filter classes for models."""

# third party
import rest_framework_filters as filters

# django app
from .models import Appointment


class AppointmentFilterset(filters.FilterSet):
    """Custom lookup filter for all fields."""

    provided = filters.CharFilter(method="get_staff")

    class Meta:
        """Meta class for model."""

        model = Appointment
        fields = {
            "id": ["exact", "in"],
            "name": ["exact", "icontains"],
            "surname": ["exact", "icontains"],
            "phone": ["exact", "icontains"],
            "app_date": ["exact", "icontains"],
            "app_time": ["exact", "icontains"],
        }

    def get_staff(self, queryset, name, value):
        """Filter method to get data."""
        print("Queryset", queryset)
        print("name is", name)
        print("value is", value)
        return None
