from django.urls import path
from .views import SearchResultsView, HomepageView
from . import views

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomepageView.as_view(), name='home'),
    path('login/', views.login_user, name='login_user'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout')
]