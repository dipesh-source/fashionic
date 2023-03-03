"""Model.py to desing the database."""
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.utils.translation import gettext as _


class CustomUserManager(BaseUserManager):
    """CustomUserManager for a model."""

    def _create_user(
        self, email, username, password=None, password2=None, **extra_fields
    ):
        """Create and saves a User with the given email, date of birth and password."""  # noqa: E501
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, email, username, password=None, password2=None, **extra_fields
    ):
        """Create a normal user."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        # extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, username, password, **extra_fields)


class CustomUser(AbstractUser):
    """Have create a custom user authentication."""

    logo = models.ImageField(upload_to="logo/", null=True, blank=True)
    email = models.EmailField(
        _("email address"),
        max_length=255,
        unique=True,
    )
    username = models.CharField(unique=True, max_length=20)
    phone = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=100)
    start_date = models.DateField(max_length=20, null=True, blank=True)
    end_date = models.DateField(max_length=20, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "phone"]

    def __str__(self):
        """Return a email while saving a data."""
        return self.email

    # def has_perm(self, perm, obj=None):
    #     "Does the user have a specific permission?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # def has_module_perms(self, app_label):
    #     "Does the user have permissions to view the app `app_label`?"
    #     # Simplest possible answer: Yes, always
    #     return True

    # @property
    # def is_staff(self):
    #     "Is the user a member of staff?"
    #     # Simplest possible answer: All admins are staff
    #     return self.is_admin
