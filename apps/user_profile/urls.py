from django.conf.urls import url
from apps.user_profile import views as profile_views


urlpatterns = [
    url(r'^$', profile_views.profile, name='profile'),
    url(r'^edit/$', profile_views.edit_profile, name='edit_profile')
]
