from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.db import transaction
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Quote, Book, FactAuthor, LifeFact, UserBook
from django.core.paginator import Paginator
import random
import requests

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
def user_library(request):
    user_books = UserBook.objects.filter(user=request.user)
    total_books = user_books.count()  # Calculer le nombre total de livres

    paginator = Paginator(user_books, 1)  # Afficher un livre par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'userbook': page_obj.object_list[0] if page_obj.object_list else None,  # Obtenir le premier livre
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'page': page_obj.number,
        'total_books': total_books,  # Nombre total de livres
    }
    return render(request, 'library.html', context)

@login_required
def challenge(request):
   return render(request, "challenge.html")

@login_required
def citation_quiz(request):
    if request.method == 'POST':
        # Récupérer la citation stockée dans la session
        quote_id = request.session.get('quote_id')
        
        # Vérifier si la citation est toujours dans la session
        if not quote_id:
            return redirect('citation_quiz')  # Rediriger si aucune citation en session
        
        quote = Quote.objects.get(id=quote_id)
        
        # Comparer la réponse de l'utilisateur avec l'auteur de la citation
        user_answer = request.POST.get('author')
        correct = user_answer == quote.author


        # Mettre à jour le score de l'utilisateur
        user_profile = UserProfile.objects.get(user=request.user)

        if correct:
            user_profile.score += 1  # Ajoute un point pour une bonne réponse
        else:
            user_profile.score -= 0.5  # Soustrait un demi-point pour une mauvaise réponse

        user_profile.save()  # Sauvegarde le score mis à jour

        # Supprimer l'ID de la citation de la session après la réponse
        del request.session['quote_id']

        # Afficher la page de résultat
        return render(request, 'resultCitation.html', {
            'quote': quote,
            'correct': correct,
            'user_answer': user_answer,
            'score': user_profile.score  # Afficher le score mis à jour
        })

    # Récupérer une citation aléatoire pour deviner l'auteur
    quote = random.choice(Quote.objects.all())

    # Stocker l'ID de la citation dans la session
    request.session['quote_id'] = quote.id

    # Récupérer tous les autres auteurs, exclure l'auteur de la citation actuelle
    other_authors = list(Quote.objects.exclude(author=quote.author).values_list('author', flat=True).distinct())

    # Si le nombre d'autres auteurs est inférieur à 3, on ajuste
    num_fake_authors = min(3, len(other_authors))

    # Sélectionner des faux auteurs et les combiner avec le vrai auteur
    fake_authors = random.sample(other_authors, num_fake_authors)
    options = fake_authors + [quote.author]

    # Mélanger les options pour que le bon auteur ne soit pas toujours à la même position
    random.shuffle(options)

    # Afficher la page du quiz avec la citation
    return render(request, 'citation.html', {
        'quote': quote,
        'options': options
    })


@login_required
def guess_book_title(request):
    if request.method == 'POST':
        # Récupérer le livre stocké dans la session
        book_id = request.session.get('book_id')
        
        # Vérifier si le livre est toujours dans la session
        if not book_id:
            return redirect('guess_book_title')  # Rediriger si aucun livre en session
        
        book = Book.objects.get(id=book_id)
        
        # Comparer la réponse de l'utilisateur avec le titre du livre
        user_answer = request.POST.get('title').strip().lower()
        correct = user_answer == book.title.strip().lower()

        # Mettre à jour le score de l'utilisateur
        user_profile = UserProfile.objects.get(user=request.user)

        if correct:
            user_profile.score += 1  # Ajoute un point pour une bonne réponse
        else:
            user_profile.score -= 0.5  # Soustrait un demi-point pour une mauvaise réponse

        user_profile.save()  # Sauvegarde le score mis à jour

        # Supprimer l'ID du livre de la session après avoir traité la réponse
        del request.session['book_id']

        # Afficher la page de résultat
        return render(request, 'result_book_guess.html', {
            'book': book,
            'correct': correct,
            'user_answer': user_answer,
            'score': user_profile.score  # Afficher le score mis à jour
        })

    # Récupérer un livre aléatoire pour deviner le titre
    book = random.choice(Book.objects.all())

    # Stocker l'ID du livre dans la session
    request.session['book_id'] = book.id

    # Afficher la page du jeu avec le résumé
    return render(request, 'guess_book_title.html', {
        'book': book
    })


@login_required
def fact_quiz(request):
    # Si c'est une requête POST, récupérer l'ID de l'affirmation depuis la session
    if request.method == 'POST':
        fact_id = request.session.get('fact_id')
        fact = LifeFact.objects.get(id=fact_id)

        selected_author_id = request.POST.get('author')
        selected_author = FactAuthor.objects.get(id=selected_author_id)

        # Vérifier si l'auteur sélectionné est le faux auteur
        correct = selected_author == fact.false_author

        # Mettre à jour le score de l'utilisateur
        user_profile = UserProfile.objects.get(user=request.user)

        if correct:
            user_profile.score += 1  # Ajoute un point pour une bonne réponse
        else:
            user_profile.score -= 0.5  # Soustrait un demi-point pour une mauvaise réponse

        user_profile.save()  # Sauvegarde le score mis à jour


        # Effacer l'ID de la session après utilisation
        del request.session['fact_id']

        return render(request, 'result_fact_quiz.html', {
            'fact': fact,
            'correct': correct,
            'selected_author': selected_author,
            'false_author': fact.false_author,
            'score': user_profile.score  # Afficher le score mis à jour
        })

    # Pour GET, récupérer une affirmation aléatoire
    fact = random.choice(LifeFact.objects.all())

    # Récupérer les vrais auteurs et l'ajouter à la liste avec le faux auteur
    true_authors = list(fact.true_authors.all())
    options = true_authors + [fact.false_author]

    # Mélanger les options pour que le faux auteur ne soit pas toujours à la même position
    random.shuffle(options)

    # Sauvegarder l'ID de l'affirmation dans la session
    request.session['fact_id'] = fact.id

    return render(request, 'fact_quiz.html', {
        'fact': fact,
        'options': options
    })


#Gestion de la Bibliothèque
def search_books(query):
    api_url = f"https://www.googleapis.com/books/v1/volumes?q={query}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json().get('items', [])
    else:
        return []

@login_required
def search_books_view(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        results = search_books(query)  # Recherche des livres à partir de l'API

    # Pagination
    paginator = Paginator(results, 4)  # Afficher 5 livres par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_books.html', {
        'results': page_obj,
        'query': query,
        'has_previous': page_obj.has_previous(),
        'has_next': page_obj.has_next(),
        'page': page_obj.number,
    })

@login_required
def add_to_library(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        title = request.POST.get('title')
        authors = request.POST.get('authors')

        # Créer ou récupérer le livre
        book, created = Book.objects.get_or_create(title=title)

        # Ajouter le livre à la bibliothèque de l'utilisateur
        UserBook.objects.create(
            user=request.user,
            book=book
        )

        return redirect('user_library')

@login_required
def update_userbook(request, userbook_id):
    userbook = get_object_or_404(UserBook, id=userbook_id)

    if request.method == 'POST':
        userbook.rating = request.POST.get('rating')
        userbook.comment = request.POST.get('comment')
        userbook.save()

        return redirect('user_library')

    return render(request, 'update_userbook.html', {'userbook': userbook})
