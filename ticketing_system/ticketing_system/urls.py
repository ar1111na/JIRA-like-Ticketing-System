"""
URL configuration for ticketing_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

# Import required settings for serving media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.homepage), #no need yet
    path('calendar/', views.calendar_view),
    path('users/', include('users.urls')),
    path('api/', include('tickets.urls')),  # Include API routes
    path('tickets/', include('tickets.urls')),   # Include HTML routes for ticket management
    path('notifications/', include('ticket_notifications.urls')),
    path('', include('dashboard.urls')),
]

# Add static media URL configuration
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)