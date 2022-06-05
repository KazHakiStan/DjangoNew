from .models import Post
from django.forms import ModelForm, TextInput, Textarea, CheckboxInput, FileInput


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'is_public', 'image']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите текст'
            }),
            'is_public': CheckboxInput(),
            'image': FileInput()
        }