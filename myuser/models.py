# flake8: noqa E501

"""Design a database relationship for system."""
from django.db import models
from django.conf import settings
from .managers import (
    AppointmentManager,
    ServiceManager,
    StaffManager,
    FeedbackManager,
    ProductManager,
    PurchaseManager,
    GalleryManager,
    AttendanceManager,
)


User = settings.AUTH_USER_MODEL


class Common(models.Model):
    """Table will store common fields data like when data is created and updated at last time."""

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        """Meta class for a common."""

        abstract = True


class Service(Common):
    """It will store all the available service of all salon."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="service",  # noqa: E501
    )
    img = models.ImageField(upload_to="service/", null=True, blank=True)
    name = models.CharField(max_length=20)
    cost = models.PositiveIntegerField()
    text = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="write about these service",  # noqa: E501
    )
    objects = models.Manager()
    objectsService = ServiceManager()

    def __str__(self) -> str:
        """Return a name."""
        return self.name


class Staff(Common):
    """Will record all the staff private and public information."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="staff",  # noqa: E501
    )
    profile = models.ImageField(upload_to="profile/")
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    specialization = models.CharField(max_length=50)
    objects = models.Manager()
    objectStaff = StaffManager()

    def __str__(self):
        """Return a name and surname."""
        return self.name + " " + self.surname

    @property
    def staff_name(self):
        """Return a staff name."""
        return self.name + " " + self.surname


class Appointment(Common):
    """This appointment class will store all the customer appointment."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="appointment",
    )
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    app_date = models.DateField(max_length=20)
    app_time = models.TimeField(max_length=10)
    # need to add service_name from Query by front-end
    service = models.ManyToManyField(
        Service, blank=True, related_name="app_service"
    )  # noqa: E501
    # need to add staff_name from Query by front-end
    provided = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="app_staff",
    )
    objects = models.Manager()
    objectsAppointment = AppointmentManager()

    def __str__(self):
        """Returning a full name while saving data"""
        return self.name + " " + self.surname

    @property
    def full_name(self):
        """Returning a full name."""
        return self.name + " " + self.surname


class Feedback(Common):
    """Customer will give the feedback by sending email for the salon service."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="feedback"
    )
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    feedback = models.TextField(max_length=1000)
    objects = models.Manager()
    objectsFeedback = FeedbackManager()

    def __str__(self) -> str:
        """Returning a name of user feedback."""
        return self.name


class Product(Common):
    """Will record all the available product for a sale in salon."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="product",  # noqa: E501
    )
    img = models.ImageField(upload_to="product/", null=True, blank=True)
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    stock = models.IntegerField()
    objects = models.Manager()
    note = models.CharField(
        max_length=100, null=True, blank=True, help_text="write note about product"
    )
    objectsProduct = ProductManager()

    def __str__(self):
        """Return a name."""
        return self.name

    @property
    def get_product(self):
        """Return a name and price."""
        return self.name + " " + self.price


class Purchase(Common):
    """Have a relationship with product table to get data of customer who have buy a product."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="purchase",  # noqa: E501
    )
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, related_name="product"
    )
    # need to add product_name to modelform
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    qty = models.IntegerField(default=1)
    objects = models.Manager()
    objectsPurchase = PurchaseManager()

    def __str__(self):
        """Return a name of customer."""
        return self.name

    def purchase_data(self):
        """Return a purchase_data."""
        return self.name + " " + self.phone + " " + self.qty


class Gallery(Common):
    """Salon owner can store his Gallery Like Images or files to the model."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="gallery",  # noqa: E501
    )
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to="gallery/", null=True)
    file = models.FileField(upload_to="files/", null=True)
    about = models.TextField(
        max_length=1000,
        null=True,
        blank=True,
        help_text="something about gallery (Images or Files)",
    )
    objects = models.Manager()
    objectsGallery = GalleryManager()


class Attendance(Common):
    """It will take a attedance for a whole staff of the salon."""

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="attendance",  # noqa: E501
    )
    staff = models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="staff_attendance",
    )
    date = models.DateField()
    is_present = models.BooleanField(default=False, null=True, blank=True)
    objects = models.Manager()
    objectsAttendance = AttendanceManager()
