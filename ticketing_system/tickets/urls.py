from django.urls import path
from . import views

urlpatterns = [
    # Add some basic URL to avoid errors, for example, a simple homepage for tickets
    path('', views.home, name='test'),
]