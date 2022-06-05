from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, PasswordInput, EmailInput


class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ник'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Почта'
            }),
            'password': PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Пароль'
            })
        }

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Ник',
        'class': 'form-control'
    }))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'пароль',
        'class': 'form-control',
        'data-toggle': 'password',
        'id': 'password',
        'name': 'password'
    }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']