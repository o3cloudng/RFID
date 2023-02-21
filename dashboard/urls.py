from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path("", dashboard, name="dashboard"),
    # path('login/', LoginView.as_view(
    #        template_name='dashboard/login.html',
    #        redirect_authenticated_user=True),
    #     name='login'),
    # path('login/', auth_views.LoginView.as_view(
    #     template_name='dashboard/login.html',
    #     redirect_authenticated_user=True), name="login"),
    path('login/', login_page, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
]
