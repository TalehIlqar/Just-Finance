import os
from datetime import datetime

from django.conf import settings


class LoggingMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def get_file_path(self):
        file_path = os.path.join(settings.BASE_DIR, "logs")
        if not os.path.exists(file_path):
            os.makedirs(file_path)
        return file_path

    def get_file_name(self):
        return datetime.now().strftime("%Y-%m-%d")

    def __call__(self, request):
        response = self.get_response(request)
        file_path = self.get_file_path()
        file_name = self.get_file_name()
        with open(os.path.join(file_path, file_name), "a") as f:
            f.write(f"{request.__dict__}{response.__dict__}")
        return response
