from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from helpers.models import TrackingModel



class Device(models.Model):
    location = models.CharField(_("Location of Device"), max_length=20, blank=False)
    device_id = models.CharField(_("Device ID"), max_length=20, blank=False)
    decription = models.CharField(_("Device description"), max_length=200, blank=False)

    def __str__(self):
        return self.location
