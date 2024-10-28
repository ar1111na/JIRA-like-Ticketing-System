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

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Authenticate and get the user
            user = form.get_user()
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect("/users/profile/")
            else:
                form.add_error(None, "Invalid login credentials. Please try again.")
        else:
            form.add_error(None, "Invalid form submission. Please try again.")

    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {"form": form})


@login_required(login_url='/users/login/')  
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")
    