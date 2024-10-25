from django.db import models
from django.contrib.auth.models import User

# Ticket model to represent an issue or a task
class Ticket(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
        ('Critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Closed', 'Closed'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Open')
    assignee = models.ForeignKey(User, related_name='assigned_tickets', on_delete=models.SET_NULL, null=True, blank=True)
    reporter = models.ForeignKey(User, related_name='reported_tickets', on_delete=models.CASCADE)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# Comment model to allow users to comment on tickets for better collaboration
class Comment(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.ticket.title}"

# Attachment model to allow users to attach files to tickets
class Attachment(models.Model):
    ticket = models.ForeignKey(Ticket, related_name='attachments', on_delete=models.CASCADE)
    file_path = models.FileField(upload_to='attachments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Attachment for {self.ticket.title}"
