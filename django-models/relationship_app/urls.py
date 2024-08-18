from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import admin_view, forbidden_view, librarian_view, list_books, LibraryDetailView, member_view
from . import views

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'),
         name='logout'),
    path('admin-view/', admin_view, name='admin-view'),
    path('librarian-view/', librarian_view, name='librarian-view'),
    path('member-view/', member_view, name='member-view'),
    path('forbidden/', forbidden_view, name='forbidden-view'),
]
