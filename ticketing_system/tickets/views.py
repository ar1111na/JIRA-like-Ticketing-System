from rest_framework import viewsets, generics
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket, Comment, Attachment
from .serializers import TicketSerializer, CommentSerializer, AttachmentSerializer
from .forms import TicketForm, CommentForm, AttachmentForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json
from django.contrib.auth.models import User 


# ViewSet for Ticket model to handle CRUD operations (API endpoints)
class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

# ViewSet for Comment model to handle CRUD operations (API endpoints)
class CommentViewSet(viewsets.ModelViewSet): 
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
    users = User.objects.all()  # Retrieve all users to use as assignees
    if request.method == 'POST':
        # Add debug print statements
        print("POST data:", request.POST)
        print("FILES:", request.FILES)
        
        # Create a copy of POST data to modify
        post_data = request.POST.copy()
        
        # If status is not provided, set default to 'Open'
        if not post_data.get('status'):
            post_data['status'] = 'Open'
            
        form = TicketForm(post_data, request.FILES)
        if form.is_valid():
            print("Form is valid")
            ticket = form.save(commit=False)
            ticket.reporter = request.user  # Set the reporter as the logged-in user
            
            # Set the assignee if provided
            assignee_id = request.POST.get('assignee')
            if assignee_id:
                try:
                    ticket.assignee = User.objects.get(id=assignee_id)
                except User.DoesNotExist:
                    print(f"User with id {assignee_id} not found")
                    return render(request, 'tickets/create_ticket.html', {
                        'form': form,
                        'users': users,
                        'error': 'Invalid assignee selected'
                    })
            
            try:
                # Save the ticket
                ticket.save()
                print(f"Ticket created with ID: {ticket.id}")
                
                # Handle attachments if they exist
                if request.FILES.get('attachments'):
                    attachment = Attachment(
                        ticket=ticket,
                        file_path=request.FILES['attachments']
                    )
                    attachment.save()
                    print(f"Attachment saved for ticket {ticket.id}")
                
                # Redirect to ticket list after successful creation
                return redirect('ticket_list')
                
            except Exception as e:
                print(f"Error saving ticket: {str(e)}")
                return render(request, 'tickets/create_ticket.html', {
                    'form': form,
                    'users': users,
                    'error': f'Error creating ticket: {str(e)}'
                })
        else:
            print("Form errors:", form.errors)
            return render(request, 'tickets/create_ticket.html', {
                'form': form,
                'users': users,
                'error': 'Please correct the errors below'
            })
    else:
        # For GET requests, create a new empty form
        form = TicketForm()

    # Context for rendering the template
    context = {
        'form': form,
        'users': users,
    }
    return render(request, 'tickets/create_ticket.html', context)


# Function-based view to update an existing ticket
def update_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    users = User.objects.all()  # Retrieve all users to use as assignees
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/update_ticket.html', {'form': form, 'ticket': ticket, 'users': users})

@login_required
def delete_ticket(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == 'POST':
        ticket.delete()
        return HttpResponseRedirect(reverse('ticket_list'))

    return render(request, 'tickets/delete_ticket.html', {'ticket': ticket})

@login_required
@csrf_exempt
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
        'file_path': attachment.file_path.url,
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

