from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TicketViewSet, CommentViewSet, AttachmentViewSet, TicketDetailAPIView, 
    create_ticket, update_ticket, add_comment, add_attachment, ticket_list, delete_ticket
)
from .views import ticket_detail_api
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

# API router for ticket management
router = DefaultRouter()
router.register(r'tickets', TicketViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'attachments', AttachmentViewSet)

# Define urlpatterns for both API and HTML views
'''
urlpatterns = [
    # Other URL patterns for your application
    path('api/', include(router.urls)),
    path('', ticket_list, name='ticket_list'),
    path('api/<int:ticket_id>/', ticket_detail_api, name='ticket_detail_api'),
    path('create/', create_ticket, name='create_ticket'),
    path('update/<int:pk>/', update_ticket, name='update_ticket'),
    path('delete/<int:pk>/', delete_ticket, name='delete_ticket'),
    path('<int:ticket_id>/comment/', add_comment, name='add_comment'),
    path('<int:ticket_id>/attachment/', add_attachment, name='add_attachment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''
urlpatterns = [
    path('api/', include(router.urls)),
    path('', ticket_list, name='ticket_list'),
    path('api/<int:ticket_id>/', ticket_detail_api, name='ticket_detail_api'),
    path('create/', create_ticket, name='create_ticket'),
    path('update/<int:pk>/', update_ticket, name='update_ticket'),
    path('delete/<int:pk>/', delete_ticket, name='delete_ticket'),
    path('<int:ticket_id>/comment/', add_comment, name='add_comment'),
    path('<int:ticket_id>/attachment/', add_attachment, name='add_attachment'),
]