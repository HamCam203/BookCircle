from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
   return render(request, "home.html")

def account(request):
   return render(request, "account.html")

def library(request):
   return render(request, "library.html")

def challenge(request):
   return render(request, "challenge.html")
