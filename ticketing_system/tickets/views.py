from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Comment, Attachment
from .serializers import TicketSerializer, CommentSerializer, AttachmentSerializer
from .forms import TicketForm, CommentForm, AttachmentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json

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

def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.delete()
    return HttpResponseRedirect(reverse('ticket_list'))
'''
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
'''
@login_required
@csrf_exempt  # Remove for production, add CSRF handling properly.
def add_comment(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse the incoming JSON data
            form = CommentForm(data)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.ticket = ticket
                comment.user = request.user
                comment.save()

                # Prepare response data
                comments = ticket.comments.all()
                comments_data = [
                    {
                        'user': comment.user.username,
                        'comment_text': comment.comment_text,
                        'created_at': comment.created_at.strftime('%Y-%m-%d')
                    }
                    for comment in comments
                ]
                return JsonResponse({'success': True, 'comments': comments_data}, status=200)
            else:
                return JsonResponse({'success': False, 'message': 'Form data is invalid'}, status=400)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON'}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method'}, status=405)

@login_required
@csrf_exempt
def add_attachment(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    if request.method == 'POST' and request.FILES:
        form = AttachmentForm(request.POST, request.FILES)
        if form.is_valid():
            attachment = form.save(commit=False)
            attachment.ticket = ticket
            attachment.save()

            attachments = ticket.attachments.all()
            attachments_data = [
                {
                    'file_path': attachment.file_path.url,
                    'uploaded_at': attachment.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')
                }
                for attachment in attachments
            ]
            return JsonResponse({'success': True, 'attachments': attachments_data}, status=200)
        else:
            return JsonResponse({'success': False, 'message': 'Form data is invalid'}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method or no file provided'}, status=405)

def ticket_detail_api(request, ticket_id):
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    # Get all comments related to this ticket
    comments = ticket.comments.all()
    comments_data = [
        {
            'user': comment.user.username,
            'comment_text': comment.comment_text,
            'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
        for comment in comments
    ]

    # Get all attachments related to this ticket
    attachments = ticket.attachments.all()
    attachments_data = [
    {
        'file_path': attachment.file_path.url,  # Use `.url` to get the complete URL of the attachment
        'uploaded_at': attachment.uploaded_at.strftime('%Y-%m-%d %H:%M:%S')
    }
    for attachment in attachments
]

    data = {
        'title': ticket.title,
        'description': ticket.description,
        'priority': ticket.priority,
        'status': ticket.status,
        'assignee': {'username': ticket.assignee.username} if ticket.assignee else None,
        'reporter': {'username': ticket.reporter.username} if ticket.reporter else None,
        'due_date': ticket.due_date.strftime("%d-%m-%Y") if ticket.due_date else None,
        'comments': comments_data,
        'attachments': attachments_data
    }
    return JsonResponse(data)


class TicketDetailAPIView(RetrieveAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

