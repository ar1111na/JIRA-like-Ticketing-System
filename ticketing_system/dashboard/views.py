
from django.shortcuts import render
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from .models import Ticket
from tickets.models import Ticket
import json
from django.contrib.auth.decorators import login_required


def count_priorities():
    total_tickets = Ticket.objects.count()  # Total number of tickets
    priority_counts = Ticket.objects.values('priority').annotate(count=Count('priority'))
    
    # Calculate count and percentage for each priority level
    counts_and_percentages = {
        'Low': {'count': 0, 'percentage': 0},
        'Medium': {'count': 0, 'percentage': 0},
        'High': {'count': 0, 'percentage': 0},
        'Critical': {'count': 0, 'percentage': 0},
    }

    for priority in priority_counts:
        priority_level = priority['priority']
        count = priority['count']
        percentage = (count / total_tickets * 100) if total_tickets > 0 else 0
        counts_and_percentages[priority_level] = {'count': count, 'percentage': round(percentage, 2)}

    return counts_and_percentages



@login_required(login_url='/users/login/')  
def dashboard(request):
    tickets = Ticket.objects.all()
    priority_counts = count_priorities()  # Get counts and percentages
    open_tickets_count = Ticket.objects.filter(status='Open').count()
    in_progress_tickets_count = Ticket.objects.filter(status='In Progress').count()
    resolved_tickets_count = Ticket.objects.filter(status='Resolved').count()
    closed_tickets_count = Ticket.objects.filter(status='Closed').count()
    
    return render(request, 'dashboard/dashboard.html', {
        'tickets': tickets,
        'priority_counts': priority_counts,
        'open_tickets_count': open_tickets_count,
        'in_progress_tickets_count': in_progress_tickets_count,
        'resolved_tickets_count': resolved_tickets_count,
        'closed_tickets_count': closed_tickets_count,
    })

@csrf_exempt
def update_ticket_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        ticket_id = data.get('ticket_id')
        new_status = data.get('new_status')

        try:
            ticket = Ticket.objects.get(id=ticket_id)
            ticket.status = new_status
            ticket.save()
            return JsonResponse({"status": "success"})
        except Ticket.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Ticket not found"})
    return JsonResponse({"status": "error", "message": "Invalid request"})


@login_required(login_url='/users/login/')  
def metrics(request):
    tickets = Ticket.objects.all()
    priority_counts = count_priorities()  # Get counts and percentages
    open_tickets_count = Ticket.objects.filter(status='Open').count()
    in_progress_tickets_count = Ticket.objects.filter(status='In Progress').count()
    resolved_tickets_count = Ticket.objects.filter(status='Resolved').count()
    closed_tickets_count = Ticket.objects.filter(status='Closed').count()
    
    return render(request, 'dashboard/metrics.html', {
        'tickets': tickets,
        'priority_counts': priority_counts,
        'open_tickets_count': open_tickets_count,
        'in_progress_tickets_count': in_progress_tickets_count,
        'resolved_tickets_count': resolved_tickets_count,
        'closed_tickets_count': closed_tickets_count,
    })


@login_required(login_url='/users/login/')  
def board(request):
    tickets = Ticket.objects.all()
    priority_counts = count_priorities()  # Get counts and percentages
    open_tickets_count = Ticket.objects.filter(status='Open').count()
    in_progress_tickets_count = Ticket.objects.filter(status='In Progress').count()
    resolved_tickets_count = Ticket.objects.filter(status='Resolved').count()
    closed_tickets_count = Ticket.objects.filter(status='Closed').count()
    
    return render(request, 'dashboard/board.html', {
        'tickets': tickets,
        'priority_counts': priority_counts,
        'open_tickets_count': open_tickets_count,
        'in_progress_tickets_count': in_progress_tickets_count,
        'resolved_tickets_count': resolved_tickets_count,
        'closed_tickets_count': closed_tickets_count,
    })








