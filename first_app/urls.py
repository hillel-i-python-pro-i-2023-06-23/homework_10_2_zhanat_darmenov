# first_app/urls.py

from django.urls import path  # , include
from first_app import views

urlpatterns = [
    path("", views.start_page, name="start_page"),
    # path("employee-list/", views.show_employees_list, name="show_employees_list"),
    # path("<str:username>/<int:age>/", views.user_information, name="user_information"),
    path("employee-list/<int:number>/", views.show_employees_list, name="show_employees_list"),
]
