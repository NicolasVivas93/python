# In this file, we will add the URL pattern for our blog application so that we can access it via the admin interface

from django.urls import path
from . import views

urlpatterns = [
    path('$/', views.posts, name='posts'),
    path('$/', views.comments, name='comments'),
]

# These are the URL pattern expressions needed to allow our application to access the views for Posts and Comments