from django import forms
from django.forms import ModelForm

from apps.user_profile.models import Profile


class GetProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth',
                  'biography', 'contacts']
        widgets = {
            'first_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'last_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'biography': forms.Textarea(attrs={'readonly': 'readonly'}),
            'contacts': forms.TextInput(attrs={'readonly': 'readonly'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'datepicker',
                                                    'readonly': 'readonly'})
        }


class EditProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'date_of_birth',
                  'biography', 'contacts']
        widgets = {
            'biography': forms.Textarea,
            'date_of_birth': forms.DateInput(attrs={'class': 'datepicker'})
        }
