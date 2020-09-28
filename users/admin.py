from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.Civil_User)  # admin.site.register(user)과 같은 의미
class CivilUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "name",
                    "gender",
                    "phone_number",
                    "city",
                    "my_soldier",
                )
            },
        ),
    )

    filter_horizontal = (
        "my_soldier",
    )

    list_display = ("name",)

@admin.register(models.Soldier_User) 
class SoldierUserAdmin(UserAdmin):
    """Custom User Admin"""

    fieldsets = (
        (
            "Custom Profile",
            {
                "fields": (
                    "name",
                    "phone_number",
                    "city",
                    "military_type",
                    "enter_date",
                    "devision",
                )
            },
        ),
    )
    list_display = ("name","get_rank","military_type","devision","get_d_day","print_leave_day")

