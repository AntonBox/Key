from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from root.base_models import TimedModel


class Profile(TimedModel):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=250, blank=True, null=True)
    last_name = models.CharField(max_length=250, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    biography = models.CharField(max_length=250, blank=True, null=True)
    contacts = models.CharField(max_length=250, blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)


class Timer(TimedModel):
    path = models.CharField(max_length=250, blank=True, null=True)
    time = models.CharField(max_length=250, blank=True, null=True)


'''You can see only post_save. there is no sense to post_delete becouse it
would duplicate OneToOne field proprty that deletes profile as well'''


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
