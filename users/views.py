from users.forms import UserRegistrationForm

from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request: HttpRequest):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account has been created successfully. Please login.")
            return redirect("login")
    else:
        return render(request, "users/html/register.html", {"form": UserRegistrationForm()})


@login_required
def profile(request: HttpRequest):
    return render(request, "users/html/profile.html")
