from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def home(request: HttpRequest):
    return HttpResponse("<H1>Welcome to my blog!</H1>")
