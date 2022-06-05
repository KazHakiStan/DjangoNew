from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile_create/', views.CreateProfilePage.as_view(), name='profile_create'),
]