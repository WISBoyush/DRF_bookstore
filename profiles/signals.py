from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import User
from .models import Profile


@receiver(post_save, sender=User)
def create_or_update(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()