from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("اطلاعات اضافی", {
            "fields": (
                'is_company', 'national_id', 'company_name',
                'economic_code', 'registration_number',
                'postal_code', 'mobile'
            )
        }),
    )
