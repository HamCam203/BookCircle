import random
from django.db import IntegrityError
from bookc.models import Quote

# Liste d'auteurs et citations pour peupler la base
authors = [
    'Albert Einstein', 'Isaac Newton', 'Marie Curie', 'Mark Twain',
    'William Shakespeare', 'Charles Darwin', 'Plato', 'Confucius',
    'Leonardo da Vinci', 'Aristotle', 'Mahatma Gandhi', 'Nelson Mandela',
    'John F. Kennedy', 'Helen Keller', 'Winston Churchill', 'Eleanor Roosevelt',
    'Jane Austen', 'George Orwell', 'J.K. Rowling', 'Toni Morrison',
    'F. Scott Fitzgerald', 'Harper Lee', 'J.D. Salinger', 'Gabriel García Márquez'
]

citations = [
    "Life is like riding a bicycle. To keep your balance you must keep moving.",  # Albert Einstein
    "If I have seen further it is by standing on the shoulders of Giants.",  # Isaac Newton
    "Nothing in life is to be feared, it is only to be understood.",  # Marie Curie
    "The secret of getting ahead is getting started.",  # Mark Twain
    "To be, or not to be, that is the question.",  # William Shakespeare
    "It is not the strongest of the species that survive, but the ones most responsive to change.",  # Charles Darwin
    "Wise men speak because they have something to say; Fools because they have to say something.",  # Plato
    "It does not matter how slowly you go as long as you do not stop.",  # Confucius
    "Learning never exhausts the mind.",  # Leonardo da Vinci
    "It is the mark of an educated mind to be able to entertain a thought without accepting it.",  # Aristotle
    "Be the change that you wish to see in the world.",  # Mahatma Gandhi
    "It always seems impossible until it’s done.",  # Nelson Mandela
    "Ask not what your country can do for you—ask what you can do for your country.",  # John F. Kennedy
    "The only thing worse than being blind is having sight but no vision.",  # Helen Keller
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",  # Winston Churchill
    "You gain strength, courage, and confidence by every experience in which you really stop to look fear in the face.",  # Eleanor Roosevelt
    "It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.",  # Jane Austen
    "War is peace. Freedom is slavery. Ignorance is strength.",  # George Orwell
    "It is our choices that show what we truly are, far more than our abilities.",  # J.K. Rowling
    "The function of freedom is to free someone else.",  # Toni Morrison
    "So we beat on, boats against the current, borne back ceaselessly into the past.",  # F. Scott Fitzgerald
    "You never really understand a person until you consider things from his point of view.",  # Harper Lee
    "I am the most miserable person in the world.",  # J.D. Salinger
    "What matters in life is not what happens to you but what you remember and how you remember it.",  # Gabriel García Márquez
]


def populate_quotes():
    try:
        # Boucle sur les auteurs et citations pour les insérer dans la base de données
        for i in range(20):  # Créer 20 citations aléatoires
            author = random.choice(authors)
            citation = random.choice(citations)
            
            # Créer et sauvegarder une nouvelle citation dans la base de données
            quote = Quote(author=author, text=citation)
            quote.save()
            print(f"Ajouté : {author} - {citation}")

    except IntegrityError:
        print(f"Erreur d'intégrité lors de l'insertion de la citation.")

if __name__ == "__main__":
    populate_quotes()
