from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.main, name='home'),
    path('posts', views.posts, name='posts'),
    re_path(r'posts/tag/(?P<tag_slug>[-\w]*)/', views.posts, name='post_by_tag'),
    path('us', views.us, name='us'),
    path('create', views.PostCreateView.as_view(), name='create'),
    path('team', views.team, name='team')

]
