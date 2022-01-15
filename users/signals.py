from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance: User, created, **kwargs):  # caution the param names have to be this and this order
    """
        When new user is created we also create a profile for that user.
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance: User, created, **kwargs):
    """
        When user is save we also save the profile of that user.
    """
    instance.profile.save()
