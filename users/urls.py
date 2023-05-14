from django.urls import path

from .views import (
    ProfileListView,
)


app_name = 'users'

urlpatterns = [
    path('list/', ProfileListView.as_view(), name='list'),
]

