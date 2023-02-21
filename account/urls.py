from django.urls import path
from account.views import *

urlpatterns = [
    path("", UserList.as_view(), name="user"),
    path("create/", UserCreateForm.as_view(), name="user-create"),
    path("<str:pk>/update/", UserUpdate.as_view(), name="user-update"),
    path("<str:pk>/detail/", UserDetail.as_view(), name="user-detail"),
    path("<str:pk>/delete/", UserDelete.as_view(), name="user-delete"),
    path("my_profile/", user_profile, name="my_profile"),
    # path("login/", login, name="login"),
    path("register/", register, name="register"),
]

# urlpatterns = [
#     path("logout/", views.logout, name="logout"),
#     path("books/", views.books, name="books"),
#     path("book-single/", views.book_single, name="book-single"),
#     path("books2/", views.books2, name="books2"),
#     path("contact/", views.contact, name="contact"),
#     path("profile/", views.profile, name="profile"),
# ]
