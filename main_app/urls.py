from django.urls import path, re_path
from . import views
from main_app.api.views.posts import PostsView
from .api.views.tags import TagsView

urlpatterns = [
    path('', views.main, name='home'),
    path('posts', views.posts, name='posts'),
    re_path(r'posts/tag/(?P<tag_slug>[-\w]*)/', views.posts, name='post_by_tag'),
    path('us', views.us, name='us'),
    path('create', views.PostCreateView.as_view(), name='create'),
    path('team', views.team, name='team'),
    path('api/posts/', PostsView.as_view({'get': 'list'}), name='api-posts'),
    path('api/tags/', TagsView.as_view({'get': 'list'}), name='api-tags'),

]
