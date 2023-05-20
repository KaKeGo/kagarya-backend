from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    CustomUser,
    UserProfile,
)
from .forms import (
    UserCreationForm,
    UserChangeForm,
)

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    
    model = CustomUser
    
    list_display = ('email', 'is_active', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        ('None', {'fields': ('email', 'password',)}),
        ('Permission', {'fields': ('is_staff', 'is_superuser',)}),
        ('Dates', {'fields': ('date_created', 'last_login')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2',)
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
