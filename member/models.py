from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from helpers.models import TrackingModel
from django.urls import reverse


class Member(TrackingModel, models.Model):
    firstname = models.CharField(_("First name"), max_length=20, blank=False)
    lastname = models.CharField(_("Last name"), max_length=20, blank=False)
    email = models.CharField(_("Email Address"), max_length=255, unique=True)
    phone_number = PhoneNumberField(_("Phone number"), null=True)
    address = models.CharField(_("Address"), max_length=200, unique=True)
    parent_guardian = models.CharField(_("Parent or Guardian name"), max_length=200, unique=True)
    tag_id = models.CharField(_("Tag ID"), max_length=20, unique=True)
    notify = models.BooleanField(_("Notification"), default=False)
    is_active = models.BooleanField(_("Is Active"), default=False)

    def __str__(self):
        return self.email

