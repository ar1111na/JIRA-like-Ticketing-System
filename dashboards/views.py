# from django.shortcuts import render
# from django.db.models import Count
# from .models import Post

# def count_priorities():
#     priority_counts = Post.objects.values('piority').annotate(count=Count('piority'))
#     counts = {priority['piority']: priority['count'] for priority in priority_counts}
    
#     return {
#         'low': counts.get('low', 0),
#         'medium': counts.get('medium', 0),
#         'high': counts.get('high', 0),
#         'critical': counts.get('critical', 0),
#     }

# def dashboards(request):
#     dashboards = Post.objects.all()
#     priority_counts = count_priorities()  # Get the counts of each priority level
#     return render(request, 'dashboards/dashboards.html', {
#         'dashboards': dashboards,
#         'priority_counts': priority_counts,
#     })




from django.shortcuts import render
from django.db.models import Count
from .models import Post

def count_priorities():
    total_posts = Post.objects.count()  # Total number of posts
    priority_counts = Post.objects.values('piority').annotate(count=Count('piority'))
    
    # Calculate count and percentage for each priority level
    counts_and_percentages = {
        'low': {'count': 0, 'percentage': 0},
        'medium': {'count': 0, 'percentage': 0},
        'high': {'count': 0, 'percentage': 0},
        'critical': {'count': 0, 'percentage': 0},
    }

    for priority in priority_counts:
        priority_level = priority['piority']
        count = priority['count']
        percentage = (count / total_posts * 100) if total_posts > 0 else 0
        counts_and_percentages[priority_level] = {'count': count, 'percentage': round(percentage, 2)}

    return counts_and_percentages

def dashboards(request):
    dashboards = Post.objects.all()
    priority_counts = count_priorities()  # Get counts and percentages
    return render(request, 'dashboards/dashboards.html', {
        'dashboards': dashboards,
        'priority_counts': priority_counts,
    })










# from django.shortcuts import render
# from .models import Post

# def dashboards(request):
#     open_tickets = Post.objects.filter(status='open')
#     in_progress_tickets = Post.objects.filter(status='in_progress')
#     resolved_tickets = Post.objects.filter(status='resolved')
#     closed_tickets = Post.objects.filter(status='closed')

#     return render(request, 'dashboards/dashboards.html', {
#         'open_tickets': open_tickets,
#         'in_progress_tickets': in_progress_tickets,
#         'resolved_tickets': resolved_tickets,
#         'closed_tickets': closed_tickets,
#     })




# dashboards/views.py
# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import Post

# def dashboards(request):
#     dashboards = Post.objects.all()
#     return render(request, 'dashboards/dashboards.html', {'dashboards': dashboards})

# def update_post_status(request):
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id')
#         new_status = request.POST.get('new_status')
#         try:
#             post = Post.objects.get(id=post_id)
#             post.piority = new_status  # Update status (piority) as needed
#             post.save()
#             return JsonResponse({"status": "success"})
#         except Post.DoesNotExist:
#             return JsonResponse({"status": "error", "message": "Post not found"})
#     return JsonResponse({"status": "error", "message": "Invalid request"})















# # dashboards/views.py
# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import Post

# def dashboards(request):
#     open_tickets = Post.objects.filter(status='open')
#     in_progress_tickets = Post.objects.filter(status='in_progress')
#     resolved_tickets = Post.objects.filter(status='resolved')
#     closed_tickets = Post.objects.filter(status='closed')

#     return render(request, 'dashboards/dashboards.html', {
#         'open_tickets': open_tickets,
#         'in_progress_tickets': in_progress_tickets,
#         'resolved_tickets': resolved_tickets,
#         'closed_tickets': closed_tickets,
#     })


# def update_post_status(request):
#     if request.method == 'POST':
#         post_id = request.POST.get('post_id')
#         new_status = request.POST.get('new_status')

#         try:
#             post = Post.objects.get(id=post_id)
#             post.piority = new_status  # Update the post's priority/status
#             post.save()
#             return JsonResponse({"status": "success"})
#         except Post.DoesNotExist:
#             return JsonResponse({"status": "error", "message": "Post not found"})
#     return JsonResponse({"status": "error", "message": "Invalid request"})












# from django.shortcuts import render
# from . models import Ticket

# # Updated view to pass ticket data to the template
# def dashboards(request):
#     # Get ticket counts by status
#     open_tickets_count = Ticket.objects.filter(status='Open').count()
#     in_progress_tickets_count = Ticket.objects.filter(status='In Progress').count()
#     resolved_tickets_count = Ticket.objects.filter(status='Resolved').count()
#     closed_tickets_count = Ticket.objects.filter(status='Closed').count()

#     # Pass the counts to the template
#     context = {
#         'open_tickets_count': open_tickets_count,
#         'in_progress_tickets_count': in_progress_tickets_count,
#         'resolved_tickets_count': resolved_tickets_count,
#         'closed_tickets_count': closed_tickets_count,
#     }
#     return render(request, 'dashboards/dashboards.html', context)
