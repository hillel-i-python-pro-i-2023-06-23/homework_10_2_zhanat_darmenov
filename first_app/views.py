# first_app/views.py

from django.http import HttpResponse


def start_page(request):

    return "Hello!"


def user_information(request, username, age):
    return f"User: {username} with Age: {age}."
