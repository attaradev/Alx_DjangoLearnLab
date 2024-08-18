from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'),
         name='logout')
]
