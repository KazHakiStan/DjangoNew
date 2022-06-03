from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='home'),
    path('posts', views.posts, name='posts'),
    path('us', views.us, name='us'),
    path('create', views.create, name='create'),

]
