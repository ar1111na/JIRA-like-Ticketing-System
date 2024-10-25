from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Comment, Attachment
from .serializers import TicketSerializer, CommentSerializer, AttachmentSerializer
from .forms import TicketForm, CommentForm, AttachmentForm
from django.contrib.auth.decorators import login_required

# ViewSet for Ticket model to handle CRUD operations (API endpoints)
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# ViewSet for Comment model to handle CRUD operations (API endpoints)
class CommentViewSet(viewsets.ModelViewSet):  # Correct the typo here if it's wrong
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

# ViewSet for Attachment model to handle CRUD operations (API endpoints)
class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer

# Function-based view to list all tickets (HTML page)
def ticket_list(request):
    tickets = Ticket.objects.all()  # Retrieve all tickets from the database
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})

# Function-based view to add a new ticket
@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.reporter = request.user  # Set the reporter as the logged-in user
            ticket.save()
            return redirect('ticket_list')  # Redirect to ticket list after successful creation
    else:
        form = TicketForm()
    return render(request, 'tickets/create_ticket.html', {'form': form})

# Function-based view to update an existing ticket
def update_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/update_ticket.html', {'form': form, 'ticket': ticket})

# Function-based view to add a new comment
@login_required
def add_comment(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ticket = ticket  # Set the ticket for this comment
            comment.user = request.user  # Set the user as the currently logged-in user
            comment.save()
            return redirect('ticket_list')  # Redirect after adding a comment
    else:
        form = CommentForm()
    return render(request, 'tickets/add_comment.html', {'form': form, 'ticket': ticket})

# Function-based view to add a new attachment
@login_required
def add_attachment(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.method == 'POST':
        form = AttachmentForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.ticket = ticket  # Set the ticket for this attachment
            attachment.save()
            return redirect('ticket_list')  # Redirect to ticket list after successfully adding an attachment
    else:
        form = AttachmentForm()
    return render(request, 'tickets/add_attachment.html', {'form': form, 'ticket': ticket})