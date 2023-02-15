from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from helpers.models import TrackingModel
from django.urls import reverse

from account.managers import CustomUserManager


# MY CUSTOM USER
class User(AbstractUser, TrackingModel):

    username = None
    email = models.CharField(max_length=255, unique=True)
    phone_number = PhoneNumberField(null=True)
    address = models.CharField(max_length=200, unique=True)
    # tag_id = models.CharField(max_length=20, unique=True)
    # notify = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        ordering = ["-created_at"]
        permissions = [
            ["deactivate_user", "can deactivate user"],
            ["print_user", "can print user"],
            ["import_user", "can import user"],
            ["export_user", "can export user"],
        ]

    def __str__(self):
        return self.email

    def get_absolute_url(self, *args, **kwargs):
        return reverse("User:detail", kwargs={"email": self.email})




