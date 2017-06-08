from django import template
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from apps.user_profile.models import Profile


register = template.Library()


@register.simple_tag
def view_user(user):
    profile = get_object_or_404(Profile, user=user)
    path_to_model = reverse('admin:user_profile_profile_change',
                            args=(profile.id,))
    return path_to_model
