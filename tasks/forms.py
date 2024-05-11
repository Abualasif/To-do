from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUserModel
        fields = ('username', 'email', 'password1', 'password2')
