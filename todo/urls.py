from django.urls import path

from .views import (
    ToDoListView,
    ToDoCreateView,
)

app_name = 'todo'


urlpatterns = [
    path('list/', ToDoListView.as_view(), name='list'),
    path('create/', ToDoCreateView.as_view(), name='create'),
]
