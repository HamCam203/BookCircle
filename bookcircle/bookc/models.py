from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

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