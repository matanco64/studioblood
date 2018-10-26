from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import random


def index(request):
    return HttpResponse("Hello, Tomer. We have a site")


def get_random(request):
    return HttpResponse(random())
