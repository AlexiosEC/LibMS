from django.shortcuts import render
from django.db.models import Q
from .models import Book

# Create your views here.
def search_books(request):
    query = request.GET.get('query')
    if query:
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        results = []
    return render(request, 'search.html', {'results': results})
