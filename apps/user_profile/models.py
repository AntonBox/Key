from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from root.base_models import TimedModel
from datetime import datetime


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


class ChangeNote(TimedModel):
    changed_object = models.CharField(max_length=250, blank=True, null=True)
    act = models.CharField(max_length=250, blank=True, null=True)
    time = models.CharField(max_length=250, blank=True, null=True)


@receiver(post_save, sender=User)
@receiver(post_save, sender=Profile)
def save_change_model(sender, instance, created, **kwargs):
    if created:
        act = 'creation'
    else:
        act = 'changing'
    change_time = datetime.now()
    ChangeNote.objects.create(changed_object=instance, act=act,
                              time=change_time)


@receiver(post_delete, sender=User)
@receiver(post_delete, sender=Profile)
def delete_model(sender, instance, **kwargs):
    act = 'deleting'
    change_time = datetime.now()
    ChangeNote.objects.create(changed_object=instance, act=act,
                              time=change_time)
