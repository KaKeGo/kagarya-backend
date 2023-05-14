from django.urls import path

from .views import (
    CheckAuthenticatedView,
    ProfileListView,
)


app_name = 'users'

urlpatterns = [
    path('check_authenticated', CheckAuthenticatedView.as_view()),
    path('list/', ProfileListView.as_view(), name='list'),
]

