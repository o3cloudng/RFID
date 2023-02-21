from django.urls import path
from .views import *



urlpatterns = [
    path("", MemberList.as_view(), name="member"),
    path("create/", MemberCreateForm.as_view(), name="member-create"),
    path("<str:pk>/update/", MemberUpdate.as_view(), name="member-update"),
    path("<str:pk>/detail/", MemberDetail.as_view(), name="member-detail"),
    path("<str:pk>/delete/", MemberDelete.as_view(), name="member-delete"),
]
