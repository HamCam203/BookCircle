from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Quote
import random

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

@login_required
def account(request):
   user_profile = get_object_or_404(UserProfile, user=request.user)
   return render(request, 'account.html', {'user_profile': user_profile})

@login_required
def library(request):
   return render(request, "library.html")

@login_required
def challenge(request):
   return render(request, "challenge.html")

@login_required
def citation_quiz(request):
    if request.method == 'POST':
        user_answer = request.POST.get('author')
        quote_id = request.POST.get('quote_id')
        quote = Quote.objects.get(id=quote_id)
        
        correct = user_answer == quote.author
        return render(request, 'resultCitation.html', {
            'quote': quote,
            'correct': correct,
            'user_answer': user_answer
        })

    # Récupérer une citation aléatoire
    quote = random.choice(Quote.objects.all())

    # Récupérer tous les autres auteurs, exclure l'auteur de la citation actuelle
    other_authors = list(Quote.objects.exclude(author=quote.author).values_list('author', flat=True).distinct())

    # Si le nombre d'autres auteurs est inférieur à 3, on ajuste
    num_fake_authors = min(3, len(other_authors))
    
    # Sélectionner des faux auteurs et les combiner avec le vrai auteur
    fake_authors = random.sample(other_authors, num_fake_authors)
    options = fake_authors + [quote.author]
    
    # Mélanger les options pour que le bon auteur ne soit pas toujours à la même position
    random.shuffle(options)
    
    return render(request, 'citation.html', {
        'quote': quote,
        'options': options,
        'quote_id': quote.id
    })

