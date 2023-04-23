from django.views.generic import TemplateView, ListView
from .models import Book
from .forms import SearchForm
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q
from django.shortcuts import render

class HomepageView(TemplateView):
    template_name = 'home.html'
    form_class = SearchForm


class SearchResultsView(ListView):
    model = Book
    template_name = 'search_results.html'

    def get_queryset(self):     # new
        query = self.request.GET.get('q')
        #vector = SearchVector('author')
        #search_query = SearchQuery(query)
        
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )
        
        #object_list = Book.objects.annotate(
            #search=SearchVector('title', 'author'),
            #rank=SearchRank(vector, search_query)
        #).filter(search=SearchQuery(query))
        #).order_by('-rank')
        return object_list
        """
        return Book.objects.filter(
            #title__icontains='of'      # Hardcoding "of" filter
            Q(title__icontains='of') | Q(author__icontains='Hall')
        )
        """


def login(request):
    error = None
    if request.method == 'POST':
        # handle form submission
        pass
    else:
        # render the login form
        return render(request, 'login.html', {'error': error})