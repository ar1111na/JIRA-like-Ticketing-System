from django.shortcuts import render, redirect
from .forms import TicketForm

def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TicketForm()
    return render(request, 'dashboard/create_ticket.html', {'form': form})
