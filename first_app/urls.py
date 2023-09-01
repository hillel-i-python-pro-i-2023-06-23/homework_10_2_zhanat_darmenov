# first_app/urls.py

from django.urls import path
from first_app import views

urlpatterns = [
    path("", views.start_page, name="start_page"),
    path("<str:username>/<int:age>/", views.user_information, name="user_information"),
]
