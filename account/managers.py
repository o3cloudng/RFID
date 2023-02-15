from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# CREATE CUSTOM USER MANAGER TO BE EXTENDED BY USER
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        extra_fields.setdefault("is_active", False)
        extra_fields.setdefault("is_verified", False)
        if email is None:
            raise TypeError(_("User should have an Email"))

        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_verified", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff True")

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser True")

        return self.create_user(email=email, password=password, **extra_fields)