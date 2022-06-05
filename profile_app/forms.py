from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, EmailInput, Textarea

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите текст'
            })
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'image']
        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'last_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите текст'
            }),
            'bio': Textarea()
        }
