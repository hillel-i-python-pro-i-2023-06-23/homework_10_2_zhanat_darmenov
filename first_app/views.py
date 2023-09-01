# first_app/views.py

from django.http import HttpResponse


def start_page(request):
    return HttpResponse("Hello!")


def user_information(request, username, age):
    return HttpResponse(f"User: {username} with Age: {age}.")
