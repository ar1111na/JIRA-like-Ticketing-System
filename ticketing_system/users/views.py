from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm,ProfileForm
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
    
@login_required(login_url='/users/login/')  
def profile_view(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None  # Optional: Handle the case where the profile doesn't exist

    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'users/profile.html', context)



@login_required(login_url='/users/login/')  
def edit_profile(request):
    profile = request.user.profile
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("/users/profile/")  # Redirect to the profile page after saving
    else:
        form = ProfileForm(instance=profile)
    return render(request, "users/edit_profile.html", {"form": form})