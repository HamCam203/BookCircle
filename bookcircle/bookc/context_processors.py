# bookapp/context_processors.py

from .models import UserProfile

def leaderboard(request):
    # Récupérer tous les profils d'utilisateur avec leurs scores, triés de manière décroissante
    top_users = UserProfile.objects.select_related('user').order_by('-score')[:5]  # Limite à 10 pour éviter de surcharger l'affichage
    return {
        'leaderboard_users': top_users
    }
