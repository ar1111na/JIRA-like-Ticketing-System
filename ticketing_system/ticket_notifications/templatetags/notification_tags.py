from django import template
from ticket_notifications.models import Notification

register = template.Library()

@register.simple_tag
def unread_notifications_count(user):
    return Notification.objects.filter(user=user, is_read=False).count()