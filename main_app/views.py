from django.forms import TextInput, Textarea, CheckboxInput, FileInput
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from taggit.models import Tag
from .models import Post
from .forms import PostForm


def main(request):
    return render(request, 'main_app/main.html')


def posts(request, tag_slug=None):
    posts = Post.objects.all().filter(is_public=False)
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    context = {'title': 'Главная страница', 'posts': posts, 'tag': tag}
    return render(request, 'main_app/posts.html', context)


def us(request):
    return render(request, 'main_app/us.html')


# def create(request):
#     error = ''
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#         else:
#             error = 'Форма была неверной'
#
#     form = PostForm()
#     context = {
#         'form': form,
#         'error': error
#     }
#     return render(request, 'main_app/create.html', context)


def team(request):
    return render(request, 'main_app/team.html')


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'text', 'is_public', 'image', 'tags']
    form = PostForm()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
