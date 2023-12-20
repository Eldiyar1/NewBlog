from django.http import HttpResponse
from datetime import datetime


def hello_view(request):
    return HttpResponse("Hello! Its my project")


def current_date_view(request):
    now = datetime.now()
    return HttpResponse(now)


def goodby_view(request):
    return HttpResponse("Goodby user!")