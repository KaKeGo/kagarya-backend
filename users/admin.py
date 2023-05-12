from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User,
)
from .forms import (
    CustomUserChangeForm,
    CustomUserCreationForm,
)

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    
    model = User
    
    list_display = ('email', 'is_active', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        ('None', {'fields': ('email', 'password',)}),
        ('Permission', {'fields': ('is_staff', 'is_superuser',)}),
        ('Dates', {'fields': ('date_created', 'last_login')}),
    )


admin.site.register(User, CustomUserAdmin)
