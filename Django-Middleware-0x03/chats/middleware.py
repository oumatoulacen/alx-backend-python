import logging
from datetime import datetime
from django.http import HttpResponse


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        ''' One-time configuration and initialization. '''
        self.get_response = get_response
        self.logger = logging.getLogger('django')
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(logging.FileHandler('requests.log'))

    def __call__(self, request):
        ''' Code to be executed for each request before or after
            the view (and later middleware) are called. '''
        user = request.user if request.user.is_authenticated else 'Anonymous'
        self.logger.info(f"{datetime.now()} - User: {user} - Path: {request.path}")
        response = self.get_response(request)

        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        ''' One-time configuration and initialization. '''
        self.get_response = get_response

    def __call__(self, request):
        ''' Code to be executed for each request before or after
            the view (and later middleware) are called. '''
        now = datetime.now()
        if now.hour < 21 and now.hour > 18:
            return HttpResponse('Sorry, the service is only available from 9 to 17', status=403)
        response = self.get_response(request)

        return response
