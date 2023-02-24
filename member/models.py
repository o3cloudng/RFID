from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from helpers.models import TrackingModel
from django.urls import reverse


class Member(TrackingModel, models.Model):
    STATUS = (
        ('DAY', _('Day')),
        ('BOARDER', _('Boarder')),
    )
    SEX = (
        ('MALE', _('Male')),
        ('FEMALE', _('Female')),
    )
    firstname = models.CharField(_("First name"), max_length=20, blank=False)
    lastname = models.CharField(_("Last name"), max_length=20, blank=False)
    day_boarder = models.CharField(_("Last name"), max_length=20, choices=STATUS, default="BOARDER")
    student_age = models.IntegerField(_("Age"), blank=False)
    student_sex = models.CharField(_("Sex / Gender"), max_length=20, choices=SEX, default="FEMALE")
    parent_guardian_name = models.CharField(_("Parent or Guardian name"), max_length=200, blank=False)
    parent_guardian_phone = PhoneNumberField(_("Parent or Guardian Phone number"), null=False)
    parent_guardian_email = models.CharField(_("Parent or Guardian Email Address"), max_length=255, blank=False)
    parent_guardian_address = models.TextField(_("Parent or Guardian Address"), blank=False)
    tag_id = models.CharField(_("Tag ID"), max_length=20, unique=True)
    notify = models.BooleanField(_("Notification"), default=False)
    is_active = models.BooleanField(_("Is Active"), default=False)
    # address = models.TextField(_("Student Address"), blank=False)

    def __str__(self):
        return f"{self.tag_id} - {self.firstname} {self.lastname}"

