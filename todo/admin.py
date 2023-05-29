from django.contrib import admin

from .models import (
    ToDo,
    TodoPlan_New,
    Todo_New,
    Task_New,
)

# Register your models here.


admin.site.register([TodoPlan_New, Todo_New, Task_New])

admin.site.register([ToDo])
