from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import add_book, admin_view, delete_book, edit_book, forbidden_view, librarian_view, list_books, LibraryDetailView, member_view
from . import views

urlpatterns = [
    path('books/', list_books, name='book-list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library-detail'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'),
         name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'),
         name='logout'),
    path('admin/', admin_view, name='admin-view'),
    path('librarian/', librarian_view, name='librarian-view'),
    path('member/', member_view, name='member-view'),
    path('forbidden/', forbidden_view, name='forbidden-view'),
    path('add_book/', add_book, name='add-book'),
    path('edit_book/<int:book_id>/', edit_book, name='edit-book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete-book'),
]
