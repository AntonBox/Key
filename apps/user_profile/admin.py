from django.contrib import admin
from apps.user_profile.models import Profile, Timer


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth')


class TimerAdmin(admin.ModelAdmin):
    list_display = ('path', 'time')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Timer, TimerAdmin)
