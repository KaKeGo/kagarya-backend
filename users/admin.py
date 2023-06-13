from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    User,
    UserProfile,
)
from .forms import (
    UserCreationForm,
    UserChangeForm,
)

# Register your models here.


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    
    model = User
    
    list_display = ('email', 'is_active', 'last_login')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        ('None', {'fields': ('username', 'email', 'password',)}),
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


admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
