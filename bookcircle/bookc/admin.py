from django.contrib import admin
from .models import UserProfile, Quote, Book, FactAuthor, LifeFact

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'date_of_birth', 'score')  # Afficher le score
    search_fields = ('user__username', 'bio')  # Recherche par nom d'utilisateur et bio
    list_filter = ('date_of_birth', 'score')  # Ajout d'un filtre sur la date de naissance et le score
    ordering = ('-score',)  # Ordonner par score décroissant
    fieldsets = (
        (None, {
            'fields': ('user', 'bio', 'profile_picture', 'date_of_birth', 'score')  # Champs à afficher dans la page d'édition
        }),
    )

class QuoteAdmin(admin.ModelAdmin):
    list_display = ('get_short_text', 'author', 'book_title')  # Affiche une version abrégée du texte
    search_fields = ('author', 'book_title')  # Recherche par auteur et titre du livre
    list_filter = ('author',)  # Filtrer par auteur

    def get_short_text(self, obj):
        return f'{obj.text[:50]}...'  # Affiche uniquement les 50 premiers caractères de la citation
    get_short_text.short_description = 'Citation'

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'summary')  # Afficher le titre et le résumé
    search_fields = ('title',)  # Permettre la recherche par titre
    list_filter = ('title',)  # Filtre par titre

class LifeFactAdmin(admin.ModelAdmin):
    list_display = ('fact', 'get_true_authors', 'false_author')  # Affiche l'anecdote, les vrais auteurs et le faux auteur
    search_fields = ('fact', 'true_authors__name', 'false_author__name')  # Recherche par texte d'anecdote et nom des auteurs
    list_filter = ('true_authors', 'false_author')  # Filtrer par auteurs

    def get_true_authors(self, obj):
        return ', '.join([author.name for author in obj.true_authors.all()])  # Affiche tous les vrais auteurs
    get_true_authors.short_description = 'Auteurs concernés'

class FactAuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Afficher le nom de l'auteur
    search_fields = ('name',)  # Permettre la recherche par nom



admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Quote, QuoteAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(LifeFact, LifeFactAdmin)
admin.site.register(FactAuthor, FactAuthorAdmin)
