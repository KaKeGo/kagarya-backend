from django.urls import path

from .views import (
    ToDoListView,
    ToDoCreateView,
    ToDoUpdateView,
    ToDoDetailView,
)

app_name = 'todo'


urlpatterns = [
    path('list/', ToDoListView.as_view(), name='list'),
    path('create/', ToDoCreateView.as_view(), name='create'),
    path('detail/<slug:slug>/', ToDoDetailView.as_view(), name='detail'),
    path('<slug>/update/', ToDoUpdateView.as_view(), name='update'),
]
