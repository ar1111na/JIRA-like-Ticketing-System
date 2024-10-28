from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm
from .models import Profile
from django.contrib.auth.decorators import login_required


# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect("/")
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {"form": form})