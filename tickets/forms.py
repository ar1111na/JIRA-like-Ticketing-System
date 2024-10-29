from django import forms
from .models import Ticket, Comment, Attachment

# Form for the Ticket model
class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'status', 'assignee', 'due_date']

# Form for the Comment model
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

# Form for the Attachment model
class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['file_path']
