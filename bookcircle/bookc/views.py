from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
   return render(request, "home.html")

def account(request):
   return render(request, "account.html")

def library(request):
   return render(request, "library.html")

def challenge(request):
   return render(request, "challenge.html")
