from django.shortcuts import render
from django.db.models import Q
from .models import Book

# Create your views here.
def search_books(request):
    return render(request, 'search.html')
