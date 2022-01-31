from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.


def UserHomeView(request):
    return render(request, 'users/home.html', {})

class UserRegisterVeiw(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users-home')

