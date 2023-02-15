from django.urls import path
from . import views



urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout, name="logout"),
    path("books/", views.books, name="books"),
    path("book-single/", views.book_single, name="book-single"),
    path("books2/", views.books2, name="books2"),
    path("contact/", views.contact, name="contact"),
    path("profile/", views.profile, name="profile"),
]
