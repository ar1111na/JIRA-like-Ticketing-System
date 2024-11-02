# ticket_notifications/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        self.group_name = f'notifications_{self.user.id}'

        # Join the user group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_notification(self, event):
        # Send the notification message to WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'ticket_id': event['ticket_id'],
        }))
