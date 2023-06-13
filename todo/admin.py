from django.contrib import admin

from .models import (
    TodoPlan,
    Todo,
    Task,
)

# Register your models here.


admin.site.register([TodoPlan, Todo, Task])
