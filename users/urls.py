from django.urls import path

from .views import (
    CheckAuthenticatedView,
    CreateUserAccount,
    ProfileListView,
)


app_name = 'users'

urlpatterns = [
    path('check_authenticated', CheckAuthenticatedView.as_view()),
    path('create/', CreateUserAccount.as_view(), name='create'),
    path('list/', ProfileListView.as_view(), name='list'),
]

