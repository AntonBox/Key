import time
from apps.user_profile.models import Timer


class RequestTimerMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        request.start_time = time.time()

    def process_response(self, request, response):
        delta = time.time() - request.start_time
        Timer.objects.create(path=request.path, time=delta)
        return response

    def process_exception(self, request, exception):
        delta = time.time() - request.start_time
        Timer.objects.create(path=request.path, time=delta)

    def __call__(self, request):
        response = self.process_request(request)
        response = self.get_response(request)
        response = self.process_response(request, response)
        return response
