from django.contrib import admin
from .models import UserProfile, Quote, Book, FactAuthor, LifeFact

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'date_of_birth')  # Les colonnes à afficher
    search_fields = ('user__username', 'bio')  # Ajout d'un champ de recherche
    list_filter = ('date_of_birth',)  # Ajout d'un filtre

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Quote)
admin.site.register(Book)
admin.site.register(FactAuthor)
admin.site.register(LifeFact)