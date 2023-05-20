from django.urls import path

from .views import (
    GetCSRFToken,
    CheckAuthenticatedView,
    CreateUserAccount,
    LoginView,
    LogoutView,
    ProfileListView,
)


app_name = 'users'

urlpatterns = [
    path('csrftoken/', GetCSRFToken.as_view(), name='csrftoken'),
    path('check_authenticated/', CheckAuthenticatedView.as_view()),
    path('create/', CreateUserAccount.as_view(), name='create'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list/', ProfileListView.as_view(), name='list'),
]

