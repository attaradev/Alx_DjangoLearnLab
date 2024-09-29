from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# ListView: Retrieve all books

class BookListView(generics.ListCreateAPIView):
    """
    BookListView handles retrieving and creating books.
    Supports filtering by title, author, and publication year.
    Allows searching through title and author fields.
    Provides ordering by title and publication year.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # Fields you want to filter by
    filterset_fields = ['title', 'author', 'publication_year']
    # Fields to enable searching on
    search_fields = ['title', 'author']
    # Fields to allow ordering by
    ordering_fields = ['title', 'publication_year']
    # Default ordering
    ordering = ['title']


# DetailView: Retrieve a single book by ID


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView: Add a new book


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can create books
    permission_classes = [IsAuthenticated]


# UpdateView: Modify an existing book


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can update books
    permission_classes = [IsAuthenticated]


# DeleteView: Remove a book


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]  # Only admins can delete books
