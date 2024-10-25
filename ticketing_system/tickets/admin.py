from django.contrib import admin
from .models import Ticket, Comment, Attachment

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(Attachment)