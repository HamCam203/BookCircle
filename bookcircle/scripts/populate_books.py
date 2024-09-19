import os
import django

# Configurer Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ton_projet.settings')  # Remplace 'ton_projet' par le nom de ton projet
django.setup()

from bookc.models import Book  # Assure-toi d'importer correctement ton modèle

# Liste des livres avec des résumés variés incluant des œuvres de science-fiction populaires
books = [
    {
        "title": "1984",
        "summary": "Dans un futur dystopique, le gouvernement totalitaire contrôle la pensée des citoyens. Winston Smith tente de se rebeller contre le système."
    },
    {
        "title": "Le Meurtre de Roger Ackroyd",
        "summary": "Hercule Poirot enquête sur le mystérieux meurtre de Roger Ackroyd dans un petit village anglais, où chaque habitant semble cacher un secret."
    },
    {
        "title": "Les Misérables",
        "summary": "L'histoire épique de la rédemption de Jean Valjean, un ancien bagnard, et de la lutte pour la justice et la liberté dans la France post-révolutionnaire."
    },
    {
        "title": "Harry Potter à l'école des sorciers",
        "summary": "Harry découvre qu'il est un sorcier et part pour Poudlard, où il rencontrera ses amis et ses ennemis, et affrontera le terrible Voldemort."
    },
    {
        "title": "Le Seigneur des Anneaux : La Communauté de l'Anneau",
        "summary": "Frodon, un jeune hobbit, est chargé de détruire l'Anneau Unique, un artefact maléfique, avec l'aide de ses compagnons dans un voyage périlleux."
    },
    {
        "title": "Battle Royale",
        "summary": "Dans une société dystopique, une classe de lycéens est forcée de s'entretuer sur une île déserte. Seul un survivant pourra quitter l'île."
    },
    {
        "title": "Le Nom de la Rose",
        "summary": "Au XIVe siècle, dans une abbaye bénédictine, un moine enquête sur une série de meurtres mystérieux. La vérité semble cachée dans un manuscrit interdit."
    },
    {
        "title": "Shining",
        "summary": "L'écrivain Jack Torrance accepte un emploi d'hiver dans un hôtel isolé, mais peu à peu, l'hôtel commence à avoir une influence néfaste sur lui et sa famille."
    },
    {
        "title": "Dune",
        "summary": "Dans un futur lointain, Paul Atréides doit naviguer dans les intrigues politiques et les dangers d'une planète désertique, où une substance rare et précieuse, l'épice, est la clé du pouvoir."
    },
    {
        "title": "Naruto",
        "summary": "Naruto Uzumaki, un jeune ninja rejeté par les autres, rêve de devenir Hokage, le plus grand ninja de son village, pour prouver sa valeur."
    },
    # Œuvres de science-fiction ajoutées
    {
        "title": "Le Guide du voyageur galactique",
        "summary": "Arthur Dent, un humain ordinaire, est entraîné dans une aventure cosmique lorsque la Terre est détruite pour faire place à une autoroute hyperspatiale."
    },
    {
        "title": "Neuromancien",
        "summary": "Case, un hacker déchu, est engagé pour une ultime mission dans le cyberespace. Cette aventure va changer sa perception du monde et de lui-même."
    },
    {
        "title": "La Guerre des mondes",
        "summary": "Lorsque des Martiens envahissent la Terre avec des machines de guerre destructrices, les humains doivent lutter pour leur survie face à une force supérieure."
    },
    {
        "title": "Fondation",
        "summary": "Hari Seldon prédit la chute de l'Empire galactique et met en place la Fondation, une organisation destinée à sauver la civilisation de la barbarie."
    },
    {
        "title": "Hyperion",
        "summary": "Sept pèlerins voyagent vers la planète Hyperion, chacun portant un secret lié à la légendaire créature appelée le Gritche."
    },
    {
        "title": "L'Homme invisible",
        "summary": "Griffin, un scientifique, découvre le secret de l'invisibilité mais sombre peu à peu dans la folie et le crime en tentant de profiter de son pouvoir."
    },
    {
        "title": "Le Cycle de Mars",
        "summary": "John Carter, un vétéran de la guerre civile, est mystérieusement transporté sur Mars, où il devient un héros malgré lui au milieu des guerres martiennes."
    },
    {
        "title": "Blade Runner",
        "summary": "Rick Deckard, un chasseur de répliquants, doit traquer et éliminer des androïdes qui cherchent à vivre librement parmi les humains."
    },
    {
        "title": "Les Chroniques martiennes",
        "summary": "Des colons terriens s'installent sur Mars, mais la culture martienne mystérieuse et les conflits internes à l'humanité menacent leur survie."
    },
    {
        "title": "Le Meilleur des mondes",
        "summary": "Dans une société future où les humains sont génétiquement conditionnés, Bernard Marx remet en question l'ordre social en rencontrant un homme du passé."
    }
]

# Ajouter les livres à la base de données
for book in books:
    Book.objects.create(title=book['title'], summary=book['summary'])

print(f'{len(books)} livres ont été ajoutés avec succès !')
