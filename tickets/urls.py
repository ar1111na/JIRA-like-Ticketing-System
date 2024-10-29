from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TicketViewSet, CommentViewSet, AttachmentViewSet,
    create_ticket, update_ticket, add_comment, add_attachment, ticket_list
)

# API router for ticket management
router = DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'attachments', AttachmentViewSet)

# Define urlpatterns for both API and HTML views
urlpatterns = [
    # API routes
    path('api/', include(router.urls)),  # Routes for the REST API

    # HTML views for tickets
    path('', ticket_list, name='ticket_list'),
    path('create/', create_ticket, name='create_ticket'),  # Create a new ticket
    path('update/<int:pk>/', update_ticket, name='update_ticket'),  # Update a ticket
    path('<int:ticket_id>/comment/', add_comment, name='add_comment'),  # Add comment to ticket
    path('<int:ticket_id>/attachment/', add_attachment, name='add_attachment'),  # Add attachment to ticket
]


  

