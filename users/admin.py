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
    
    list_display = ('username', 'email', 'is_active')


admin.site.register(User, CustomUserAdmin)
