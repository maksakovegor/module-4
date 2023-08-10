from django.urls import path
from .views import index , top_sellers , advertisements_post , register , login , profile

urlpatterns = [
    path('', index),
    path('top-sellers/', top_sellers),
    path('advertisement-post/', advertisements_post),
    path('register/', register),
    path('login/', login),
    path('profile/', profile)
]