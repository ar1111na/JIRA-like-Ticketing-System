from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    role = models.CharField(max_length=50, default="user")    
    
    def __str__(self):
        return f"{self.user.username}'s profile"
    





    
    