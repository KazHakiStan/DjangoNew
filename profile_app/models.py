from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    username = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    bio = models.CharField(max_length=50, null=True, blank=True)
    subscribes = models.IntegerField(default=0)
    subscribers = models.IntegerField(default=0)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
