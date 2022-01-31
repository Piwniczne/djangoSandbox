from django.urls import path
from . import views
from .views import UserRegisterVeiw

urlpatterns = [
    path('', views.UserHomeView, name='users-home'),
    path('register/', UserRegisterVeiw.as_view(), name='users-register'),
]