from django import forms
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom', required=True)
    last_name = forms.CharField(label='Nom', required=True)
    email = forms.EmailField(label='Adresse e-mail', required=True)
    bio = forms.CharField(widget=forms.Textarea, required=False, label='Biographie')
    profile_picture = forms.ImageField(required=False, label='Photo de profil')
    date_of_birth = forms.DateField(required=False, label='Date de naissance', widget=forms.SelectDateWidget)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
