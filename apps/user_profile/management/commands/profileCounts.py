from django.core.management import BaseCommand

from apps.user_profile.models import Profile


class Command(BaseCommand):
    help = "All profile objects"

    def handle(self, *args, **options):
        profiles = Profile.objects.all().count()
        profiles = "Count of profiles: {}".format(profiles)
        self.stdout.write(profiles)
