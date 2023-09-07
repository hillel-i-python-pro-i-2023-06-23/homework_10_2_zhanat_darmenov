# first_app/views.py

from django.http import HttpResponse
from django.shortcuts import render
from collections.abc import Iterator
from typing import NamedTuple
from faker import Faker
import re

faker = Faker()


class Employee(NamedTuple):
    emp_full_name: str
    emp_email: str
    emp_password: str

    def __str__(self) -> str:
        return f"{self.emp_full_name} {self.emp_email}"


def generate_employee() -> Employee:
    sex = faker.person.sexType()
    first_name = faker.person.firstName(sex)
    last_name = faker.person.lastName()
    name_surname = f"{first_name} {last_name}"
    full_name = re.sub(r"[^a-zA-Z0-9]+", "_", name_surname).lower()
    email = faker.helpers.unique(faker.internet.email, [full_name])
    password = faker.internet.password()
    return Employee(emp_full_name=full_name, emp_email=email, emp_password=password)


def generate_some_employees(amount: int) -> Iterator[Employee]:
    for _ in range(amount):
        yield generate_employee()


def start_page(request):
    if request.POST.get("action") == "Register":
        number = request.POST.get("quantity")
        # Save rturn value and show in html.
        # Probably pass to another method
        generate_some_employees(number)
    return render(request, "start_page.html", {"message": "Hello!"})


def user_information(request, username, age):
    return HttpResponse(f"User: {username} with Age: {age}.")


def show_employees_list():
    ...
