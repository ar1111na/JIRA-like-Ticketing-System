from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=50, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')])
    status = models.CharField(max_length=50, choices=[('Open', 'Open'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved'), ('Closed', 'Closed')])
    assignee = models.ForeignKey(User, related_name='dashboard_assigned_tickets', on_delete=models.SET_NULL, null=True)
    reporter = models.ForeignKey(User, related_name='dashboard_reported_tickets', on_delete=models.SET_NULL, null=True)
    #due_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(default='2024-10-30')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    comment_text = models.TextField()
    ticket = models.ForeignKey(Ticket, related_name='dashboard_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='dashboard_comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Attachment(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='dashboard_attachments', on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.ticket.title}"
