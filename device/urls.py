from django.urls import path
from .views import *



urlpatterns = [
    path("", DeviceList.as_view(), name="device"),
    path("create/", DeviceCreateForm.as_view(), name="device-create"),
    path("<str:pk>/update/", DeviceUpdate.as_view(), name="device-update"),
    path("<str:pk>/detail/", DeviceDetail.as_view(), name="device-detail"),
    path("<str:pk>/delete/", DeviceDelete.as_view(), name="device-delete"),
]
