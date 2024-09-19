from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    score = models.FloatField(default=0)  # Nouveau champ score avec valeur par défaut 0

    def __str__(self):
        return self.user.username

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=255)
    book_title = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.text[:50]}... - {self.author}'

class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()

    def __str__(self):
        return self.title

class LifeFact(models.Model):
    fact = models.TextField()  # Anecdote de vie
    true_authors = models.ManyToManyField('FactAuthor', related_name='true_facts')  # Les auteurs pour qui l'affirmation est vraie
    false_author = models.ForeignKey('FactAuthor', on_delete=models.CASCADE, related_name='false_facts')  # L'auteur pour qui c'est faux

    def __str__(self):
        return self.fact

class FactAuthor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name