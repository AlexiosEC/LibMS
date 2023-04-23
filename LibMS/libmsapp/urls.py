from django.urls import path
from . import views
from .views import SearchBooksView

urlpatterns = [
    path('', SearchBooksView.as_view(), name='search_books'),
    path('login/', views.login, name='login'),
]
