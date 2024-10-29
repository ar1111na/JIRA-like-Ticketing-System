from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')





































# from .forms import TicketForm
# from .models import Ticket"""





# """def create_ticket(request):
#     if request.method == 'POST':
#         form = TicketForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')  # Redirect to a specific URL after saving
#     else:
#         form = TicketForm()

#     return render(request, 'create_ticket.html', {'form': form})

# def update_ticket(request, pk):
#     ticket = get_object_or_404(Ticket, pk=pk)
#     if request.method == 'POST':
#         form = TicketForm(request.POST, instance=ticket)
#         if form.is_valid():
#             form.save()
#             return redirect('homepage')
#     else:
#         form = TicketForm(instance=ticket)

#     return render(request, 'update_ticket.html', {'form': form})
