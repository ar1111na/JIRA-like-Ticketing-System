from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .forms import CustomUserCreationForm,ProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from tickets.views import Ticket   # Import for the table ticket view


# Create your views here.


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect("/users/profile/")
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
        return redirect("/dashboard/")
    
@login_required(login_url='/users/login/')
def profile_view(request):
    user = request.user
    try:
        profile = Profile.objects.get(user=user)
    except Profile.DoesNotExist:
        profile = None

    # Get tickets assigned to the current user for the table ticket view
    assigned_tickets = Ticket.objects.filter(assignee=user)

    # Counters for different ticket statuses for the table ticket view
    open_count_p = assigned_tickets.filter(status="Open").count()
    in_progress_count_p = assigned_tickets.filter(status="In Progress").count()
    resolved_count_p = assigned_tickets.filter(status="Resolved").count()
    closed_count_p = assigned_tickets.filter(status="Closed").count()

    # Define the total number of tasks, including those in different statuses for the table ticket view
    total_task_count = assigned_tickets.count()
    running_task_count = in_progress_count_p
    on_hold_task_count = resolved_count_p
    complete_task_count = closed_count_p

    # Apply filters if provided for the table ticket view for the table ticket view
    from_date = request.GET.get('from_date')
    to_date = request.GET.get('to_date')
    priority = request.GET.get('priority')

    if from_date:
        assigned_tickets = assigned_tickets.filter(created_at__gte=from_date)
    if to_date:
        assigned_tickets = assigned_tickets.filter(due_date__lte=to_date)
    if priority:
        assigned_tickets = assigned_tickets.filter(priority=priority)

    context = {
        'user': user,
        'profile': profile,
        'assigned_tickets': assigned_tickets, # for the table ticket view
        'total_task_count': total_task_count, # total number of assigned tickets for the table ticket view
        'running_task_count': running_task_count, # number of running tickets for the table ticket view
        'on_hold_task_count': on_hold_task_count, # number of tickets on hold for the table ticket view
        'complete_task_count': complete_task_count, # number of completed tickets for the table ticket view
        'open_count_p': open_count_p, # for the table ticket view
        'in_progress_count_p': in_progress_count_p, # for the table ticket view
        'resolved_count_p': resolved_count_p, # for the table ticket view
        'closed_count_p': closed_count_p, # for the table ticket view
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