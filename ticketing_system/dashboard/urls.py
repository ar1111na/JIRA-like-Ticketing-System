from django.urls import path
from . import views
from .views import (
    board, metrics
)



urlpatterns = [
    #  path('', views.dashboard),
     path('', views.metrics, name='metrics'),
     path('board/', board, name='board'),
     path('update_ticket_status/', views.update_ticket_status, name='update_ticket_status'),
 ]
  
