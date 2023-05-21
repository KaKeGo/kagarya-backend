from django.contrib import admin

from .models import ShowApiUrl, CategoryApi

# Register your models here.


admin.site.register([ShowApiUrl, CategoryApi])
