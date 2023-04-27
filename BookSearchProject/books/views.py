from django.views.generic import TemplateView, ListView
from .models import Book
from .forms import SearchForm
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.db.models import Q
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

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

@csrf_protect
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            # User exists, log them in and redirect
            login(request, user)
            return redirect('home')
        else:
            # User does not exist, display error message
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    
def logout_user(request):
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        # handle form submission
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            # messages.success(request, ("You have signed up successfully!"))
            return redirect('home')
    else:
        form = UserCreationForm()
        # render the login form
    return render(request, 'signup.html', {'form': form})