from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            with transaction.atomic():  # Utiliser une transaction pour garantir que tout est sauvegardé correctement
                user = form.save()  # Crée l'utilisateur

                # Crée ou met à jour le profil utilisateur associé
                UserProfile.objects.update_or_create(
                    user=user,
                    defaults={
                        'bio': form.cleaned_data.get('bio', ''),
                        'profile_picture': form.cleaned_data.get('profile_picture'),
                        'date_of_birth': form.cleaned_data.get('date_of_birth', None)
                    }
                )
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('home')
    else:
        form = UserRegistrationForm()

    # Séparation des champs
    user_fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
    profile_fields = ['bio', 'profile_picture', 'date_of_birth']

    return render(request, 'registration/register.html', {
        'form': form,
        'user_fields': user_fields,
        'profile_fields': profile_fields
    })



@login_required
def home(request):
   return render(request, "home.html")

def account(request):
   return render(request, "account.html")

def library(request):
   return render(request, "library.html")

def challenge(request):
   return render(request, "challenge.html")
