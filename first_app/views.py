# first_app/views.py

# from django.http import HttpResponse
# from django.urls import reverse
from django.shortcuts import render, redirect
from collections.abc import Iterator
from typing import NamedTuple
from faker import Faker
import re

faker = Faker()


class Employee(NamedTuple):
    full_name: str
    email: str
    password: str

    def __str__(self) -> str:
        return f"{self.full_name} {self.email} & {self.password}"


def generate_employee() -> Employee:
    first_name = faker.first_name()
    last_name = faker.last_name()
    name_surname = f"{first_name} {last_name}"

    return Employee(
        full_name=re.sub(r"[^a-zA-Z0-9]+", "_", name_surname).lower(), email=faker.email(), password=faker.password()
    )


def generate_some_employees(amount: int) -> Iterator[Employee]:
    for _ in range(amount):
        yield generate_employee()


def start_page(request):
    if request.method == "POST" and request.POST.get("action") == "Submit":
        quantity = request.POST.get("quantity")
        if quantity:
            number = int(quantity)
        else:
            number = 1

        return redirect(f"/employee-list/{number}/")
    print("START - = - = - = - = - = - = - = - =\n")
    return render(request, "start_page.html", {"message": "Hello!"})


def show_employees_list(request, number):
    emp_list = generate_some_employees(number)

    return render(
        request=request,
        template_name="employee_list.html",
        context=dict(emp_list=emp_list),
    )


# def user_information(request, username, age):
#     return HttpResponse(f"User: {username} with Age: {age}.")
