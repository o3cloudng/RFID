from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
from .models import User

class CustomUserAdmin(UserAdmin):
    add_form = UserForm
    form = UserChangeForm
    model = User
    list_display = ("first_name","last_name", "email", "phone_number", "address",  "is_staff", "is_active",)
    list_filter = ("first_name","last_name", "email", "phone_number", "address", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("first_name","last_name", "email","phone_number", "address", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "first_name","last_name", "email", "phone_number", "address", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(User, CustomUserAdmin)


# class MemberAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = User
#     list_display = ("firstname","lastname", "email", "phone_number", "tag_id", "address", "notify", "is_active",)
#     list_filter = ("firstname","lastname", "email", "phone_number", "tag_id", "address", "notify", "is_active",)
#     fieldsets = (
#         (None, {"fields": ("firstname","lastname", "email","phone_number", "tag_id", "address", "notify")}),
#         # ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
#     )
#     add_fieldsets = (
#         (None, {
#             "classes": ("wide",),
#             "fields": (
#                 "firstname","lastname", "email", "phone_number", "tag_id", "address", "notify", 
#                 "is_active"
#             )}
#         ),
#     )
#     search_fields = ("email",)
#     ordering = ("email",)

# admin.site.register(Member, MemberAdmin)
# admin.site.register(Member)