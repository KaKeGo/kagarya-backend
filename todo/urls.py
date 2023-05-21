from django.urls import path

from .views import (
    ToDoListView,   
)

app_name = 'todo'


urlpatterns = [
    path('list/', ToDoListView.as_view(), name='list'),
]
