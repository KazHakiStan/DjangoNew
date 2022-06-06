from django.contrib.auth.models import User
from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=50, unique=False, blank=False, null=False)
    text = models.TextField('Текст', blank=False, null=False)
    is_public = models.BooleanField('Приватный', default=False)
    likes = models.IntegerField('Лайки', default=0)
    created_at = models.DateTimeField('Создан в:', auto_now_add=True)
    image = models.ImageField('Картинки', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts')

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
