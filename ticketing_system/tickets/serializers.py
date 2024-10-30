from rest_framework import serializers
from .models import Ticket, Comment, Attachment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')  

    class Meta:
        model = Comment
        fields = ['user', 'comment_text', 'created_at']

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['file_path', 'uploaded_at']

class TicketSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  
    attachments = AttachmentSerializer(many=True, read_only=True)  

    assignee = serializers.CharField(source='assignee.username', allow_null=True)
    reporter = serializers.CharField(source='reporter.username')

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'priority', 'status', 'assignee', 'reporter', 'due_date', 'comments', 'attachments']

