from django.conf import settings


def context_settings(request):
    return {'context_settings': settings}
