from django.urls import path
from core.views import ListUser


urlpatterns = [
    path('users/', ListUser.as_view(), name='users'),
]