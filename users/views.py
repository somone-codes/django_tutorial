from users.forms import UserRegistrationForm, UserUpdationForm, ProfileUpdationForm

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

    if request.method == "POST":
        user_form = UserUpdationForm(request.POST, instance=request.user)
        profile_form = ProfileUpdationForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Profile updated!")
            return redirect("profile")

    else:
        user_form = UserUpdationForm(instance=request.user)
        profile_form = ProfileUpdationForm(instance=request.user.profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, "users/html/profile.html", context)
