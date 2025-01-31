import logging
from datetime import datetime


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
