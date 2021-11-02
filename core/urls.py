from django.urls import path
from core.views import (
    ListUser,
    RegisterUser
)


urlpatterns = [
    path('users/', ListUser.as_view(), name='users'),
    path('register/', RegisterUser.as_view(), name='register'),
]