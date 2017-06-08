from django.shortcuts import render, get_object_or_404
from apps.user_profile.forms import GetProfileForm, EditProfileForm
from django.contrib.auth.decorators import login_required
from apps.user_profile.models import Profile
from django.contrib import messages


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
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            # getting ip
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')
            obj.ip = ip
            obj.user = user
            obj.save()
            messages.add_message(
                request, messages.INFO,
                'You profile has been succesfully changed')
    return render(request, 'edit_profile.html', {'form': form})
