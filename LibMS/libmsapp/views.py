from django.shortcuts import render
from django.db.models import Q
from .models import Book
from django.http import HttpResponse
from django.views.generic import ListView
from .forms import SearchForm

# Create your views here.
class SearchBooksView(ListView):
    form_class = SearchForm
    model = Book
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        return object_list

def login(request):
    error = None
    if request.method == 'POST':
        # handle form submission
        pass
    else:
        # render the login form
        return render(request, 'login.html', {'error': error})
