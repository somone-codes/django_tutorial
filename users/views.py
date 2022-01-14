from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request: HttpRequest):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"user {username} registered successfully")
            return redirect("blog-home")
    else:
        return render(request, "users/html/register.html", {"form": UserCreationForm()})
