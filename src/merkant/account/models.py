from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .choices import UserType
from .managers import UserManager
from core.models import TimeStampedModel


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    type = models.IntegerField(choices=UserType,default=UserType.CUSTOMER)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Profile(TimeStampedModel):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(_("first name"), max_length=50, blank=True)
    last_name = models.CharField(_("last name"), max_length=50, blank=True)
    image = models.ImageField(upload_to="profile_pics", null=True, blank=True)
    bio = models.TextField(blank=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self) -> str:
        return self.full_name or self.user.email


class Address(TimeStampedModel):
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="addresses")
    title = models.CharField(_("title"), max_length=50, blank=True)   # "Home", "Work"
    recipient_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20) # you can add a validator
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20, blank=True) # you can add a validator
    is_default = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["profile"],
                condition=models.Q(is_default=True),
                name="one_default_address_per_profile",
            )
        ]

    def __str__(self):
        return f"{self.title or self.street_address}, {self.city}"
