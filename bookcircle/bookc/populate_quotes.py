import random
from django.db import IntegrityError
from bookc.models import Quote

# Liste d'auteurs par genre
authors_by_genre = {
    'Thriller': [
        'Stephen King', 'Gillian Flynn', 'Lee Child', 'Harlan Coben',
        'John Grisham', 'James Patterson', 'Dan Brown', 'Patricia Highsmith'
    ],
    'Roman Policier': [
        'Agatha Christie', 'Arthur Conan Doyle', 'Georges Simenon', 'Raymond Chandler',
        'Michael Connelly', 'Fred Vargas', 'Jean-Christophe Grangé', 'Stieg Larsson'
    ],
    'Manga': [
        'Eiichiro Oda', 'Akira Toriyama', 'Masashi Kishimoto', 'Naoki Urasawa',
        'Osamu Tezuka', 'Tite Kubo', 'Yoshihiro Togashi', 'Kentaro Miura'
    ],
    'Science-Fiction': [
        'Isaac Asimov', 'Philip K. Dick', 'Arthur C. Clarke', 'Frank Herbert',
        'Ray Bradbury', 'William Gibson', 'H.G. Wells', 'Orson Scott Card'
    ]
}

# Liste de citations fictives associées à ces genres
citations_by_genre = {
    'Thriller': [
        "The only way to survive is to keep moving forward.",
        "Some secrets are better left buried.",
        "In the shadows, truth is the deadliest weapon.",
        "Fear is the most powerful enemy of all.",
    ],
    'Roman Policier': [
        "Every clue is a step closer to the truth.",
        "Murder is only the beginning.",
        "Nothing is ever as simple as it seems.",
        "Justice may be blind, but detectives are not.",
    ],
    'Manga': [
        "Believe in the power of your dreams.",
        "The bonds we forge in life are stronger than steel.",
        "Victory comes to those who fight for their friends.",
        "Never give up, no matter how dark the path may seem.",
    ],
    'Science-Fiction': [
        "The future is not set, but our choices shape it.",
        "In the vastness of space, humanity is but a speck.",
        "Technology is a double-edged sword.",
        "To explore the stars is to explore ourselves."
    ]
}

def populate_quotes():
    try:
        total_quotes = 48  # Nombre total de citations à insérer
        genres = ['Thriller', 'Roman Policier', 'Manga', 'Science-Fiction']
        
        for _ in range(total_quotes):
            # Choisir un genre aléatoire
            genre = random.choice(genres)
            
            # Choisir un auteur et une citation au hasard dans ce genre
            author = random.choice(authors_by_genre[genre])
            citation = random.choice(citations_by_genre[genre])
            
            # Créer et sauvegarder une nouvelle citation dans la base de données
            quote = Quote(author=author, text=citation)
            quote.save()
            print(f"Ajouté : {author} ({genre}) - {citation}")
    
    except IntegrityError:
        print("Erreur d'intégrité lors de l'insertion de la citation.")

if __name__ == "__main__":
    populate_quotes()
