from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from apps.user_profile.forms import GetProfileForm, EditProfileForm
from apps.user_profile.models import Profile
from apps.user_profile.functions import get_ip


@login_required
def profile(request):
    user = request.user
    profile, _ = Profile.objects.get_or_create(user=user)
    form = GetProfileForm(initial={'first_name': profile.first_name,
                                   'last_name': profile.last_name,
                                   'date_of_birth': profile.date_of_birth,
                                   'biography': profile.biography,
                                   'contacts': profile.contacts})
    return render(request, 'profile.html', {'form': form})


@login_required
def edit_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method == 'GET':
        form = EditProfileForm(initial={'first_name': profile.first_name,
                                        'last_name': profile.last_name,
                                        'date_of_birth': profile.date_of_birth,
                                        'biography': profile.biography,
                                        'contacts': profile.contacts})
    elif request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.ip = get_ip(request)
            obj.user = user
            obj.save()
            messages.add_message(
                request, messages.INFO,
                'You profile has been succesfully changed')
    return render(request, 'edit_profile.html', {'form': form})
