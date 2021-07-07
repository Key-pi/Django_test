from django.utils import timezone

from .models import Log


class LogMiddleware(object):

    def __init__(self, get_response=None):
        self.get_response = get_response

    def __call__(self, request):
        if '/admin/' not in request.path:
            Log.objects.create(path=request.path, method=request.method, timestamp=timezone.now())
        return self.get_response(request)
