from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'date_of_birth')  # Les colonnes à afficher
    search_fields = ('user__username', 'bio')  # Ajout d'un champ de recherche
    list_filter = ('date_of_birth',)  # Ajout d'un filtre

admin.site.register(UserProfile, UserProfileAdmin)
