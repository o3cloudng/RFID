from django.urls import path
from .views import *



urlpatterns = [
    path("", ApiCreateApiView.as_view(), name="api-create"),
    # path("v2/", apidata_view, name="v2-api-create"),
]
