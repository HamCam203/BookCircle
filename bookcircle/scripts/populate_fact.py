from bookc.models import FactAuthor, LifeFact

# Créer des auteurs
a1 = FactAuthor.objects.create(name="Victor Hugo")
a2 = FactAuthor.objects.create(name="Jules Verne")
a3 = FactAuthor.objects.create(name="George Orwell")
a4 = FactAuthor.objects.create(name="Stephen King")
a5 = FactAuthor.objects.create(name="Agatha Christie")
a6 = FactAuthor.objects.create(name="Isaac Asimov")
a7 = FactAuthor.objects.create(name="Arthur Conan Doyle")
a8 = FactAuthor.objects.create(name="Haruki Murakami")
a9 = FactAuthor.objects.create(name="H.G. Wells")
a10 = FactAuthor.objects.create(name="Margaret Atwood")
a11 = FactAuthor.objects.create(name="Ray Bradbury")

# 1. Affirmation
fact1 = LifeFact.objects.create(fact="Cet auteur a vécu en exil pendant plusieurs années.", false_author=a4)
fact1.true_authors.set([a1, a2, a3])  # Hugo, Verne, Orwell
fact1.save()

# 2. Affirmation
fact2 = LifeFact.objects.create(fact="Cet auteur a travaillé comme détective privé.", false_author=a6)
fact2.true_authors.set([a7])  # Arthur Conan Doyle
fact2.save()

# 3. Affirmation
fact3 = LifeFact.objects.create(fact="Cet auteur est connu pour ses romans de science-fiction.", false_author=a5)
fact3.true_authors.set([a2, a6, a9])  # Jules Verne, Isaac Asimov, H.G. Wells
fact3.save()

# 4. Affirmation
fact4 = LifeFact.objects.create(fact="Cet auteur a reçu un prix Nobel.", false_author=a4)
fact4.true_authors.set([a1, a8, a10])  # Hugo, Murakami, Atwood
fact4.save()

# 5. Affirmation
fact5 = LifeFact.objects.create(fact="Cet auteur a écrit plus de 100 œuvres publiées.", false_author=a11)
fact5.true_authors.set([a5, a6, a1])  # Agatha Christie, Isaac Asimov, Victor Hugo
fact5.save()

# 6. Affirmation
fact6 = LifeFact.objects.create(fact="Cet auteur a été médecin.", false_author=a3)
fact6.true_authors.set([a7, a2])  # Arthur Conan Doyle, Jules Verne
fact6.save()

# 7. Affirmation
fact7 = LifeFact.objects.create(fact="Cet auteur est connu pour ses romans dystopiques.", false_author=a8)
fact7.true_authors.set([a3, a9, a10])  # George Orwell, H.G. Wells, Margaret Atwood
fact7.save()

# 8. Affirmation
fact8 = LifeFact.objects.create(fact="Cet auteur a également été scénariste pour la télévision.", false_author=a7)
fact8.true_authors.set([a4, a11, a6])  # Stephen King, Ray Bradbury, Isaac Asimov
fact8.save()

# 9. Affirmation
fact9 = LifeFact.objects.create(fact="Cet auteur a survécu à plusieurs tentatives d'assassinat.", false_author=a9)
fact9.true_authors.set([a1, a3])  # Victor Hugo, George Orwell
fact9.save()

# 10. Affirmation
fact10 = LifeFact.objects.create(fact="Cet auteur est connu pour ses récits policiers.", false_author=a6)
fact10.true_authors.set([a5, a7, a3])  # Agatha Christie, Arthur Conan Doyle, George Orwell
fact10.save()
