from django.db import models
from account.models import User
from helpers.models import TrackingModel
from member.models import Member
from device.models import Device
# Create your models here.

class ApiData(TrackingModel, models.Model):
    tag_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)


    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.tag_id} - {self.device_id.location}"