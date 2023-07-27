from django.urls import path
from .views import index , top_sellers , advertisements_post

urlpatterns = [
    path('', index),
    path('top-sellers/', top_sellers),
    path('advertisement-post/', advertisements_post)
]