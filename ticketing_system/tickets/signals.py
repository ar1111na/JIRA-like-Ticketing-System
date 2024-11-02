# tickets/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ticket
from ticket_notifications.models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@receiver(post_save, sender=Ticket)
def create_notification(sender, instance, created, **kwargs):
    if created and instance.assignee:
        Notification.objects.create(
            user=instance.assignee,
            ticket=instance,
            message=f'New ticket assigned: {instance.title}'
        )

        # Send notification through WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f'notifications_{instance.assignee.id}',
            {
                'type': 'send_notification',
                'message': f'New ticket assigned: {instance.title}',
                'ticket_id': instance.id,
            }
        )