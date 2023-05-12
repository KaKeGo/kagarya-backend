from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    CustomUser,
    UserProfile,
)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile.objects.create(
                user=instance
            )
        user_profile.save()

post_save.connect(create_user_profile, sender=CustomUser)
