from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=50, unique=False, blank=False, null=False)
    text = models.TextField('Текст', blank=False, null=False)
    is_public = models.BooleanField('Приватный', default=False)
    likes = models.IntegerField('Лайки', default=0)
    created_at = models.DateTimeField('Создан в:', auto_now_add=True)
    image = models.ImageField('Картинки', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'