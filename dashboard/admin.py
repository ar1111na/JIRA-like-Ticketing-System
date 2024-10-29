from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'priority', 'assignee', 'created_at', 'updated_at')
    list_filter = ('status', 'priority')
    search_fields = ('title', 'description')

admin.site.register(Ticket, TicketAdmin)

