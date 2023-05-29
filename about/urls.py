from django.urls import path

from .views import (
    AboutListView,
    AboutUpdateView,
)

app_name = 'about'


urlpatterns = [
    path('', AboutListView.as_view(), name='about'),
    path('<slug>/update/', AboutUpdateView.as_view(), name='update'),
]

