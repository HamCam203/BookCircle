"""bookcircle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from bookc import views
from bookc.views import home
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('home/', views.home, name="home"),
    path('account/', views.account, name="account"),
    path('challenge/', views.challenge, name="challenge"),
    path('citation/', views.citation_quiz, name='citation_quiz'),
    path('guess_book_title/', views.guess_book_title, name='guess_book_title'),
    path('fact-quiz/', views.fact_quiz, name='fact_quiz'),


    # Recherche de livres via l'API Google Books
    path('search/', views.search_books_view, name='search_books'),
    
    # Ajout d'un livre à la bibliothèque de l'utilisateur
    path('add-to-library/', views.add_to_library, name='add_to_library'),
    
    # Bibliothèque de l'utilisateur
    path('library/', views.user_library, name='user_library'),
    
    # Mise à jour d'un UserBook (note et commentaire)
    path('library/update/<int:userbook_id>/', views.update_userbook, name='update_userbook'),

    #Gestion de connexion, déconnexion et inscription
	path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
    path('register/', views.register, name='register'),
    
    #Gestion de réinitialisation du mot de passe
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name = 'password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
