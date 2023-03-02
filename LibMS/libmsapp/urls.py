from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_books, name='search_books'),
    path('login/', views.login, name='login'),
]
