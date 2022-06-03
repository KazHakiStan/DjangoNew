from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def main(request):
    return render(request, 'main_app/main.html')


def posts(request):
    posts = Post.objects.all().filter(is_public=False)
    context = {'title': 'Главная страница', 'posts': posts}
    return render(request, 'main_app/posts.html', context)


def us(request):
    return render(request, 'main_app/us.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = PostForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main_app/create.html', context)