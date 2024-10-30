# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile  # Make sure this points to your Profile model location

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:  # Only create profile for new users
        Profile.objects.create(user=instance)
