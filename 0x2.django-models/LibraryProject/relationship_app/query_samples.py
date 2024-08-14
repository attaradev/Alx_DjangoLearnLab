from relationship_app.models import Book, Library

# Query all books by a specific author.
books = Book.objects.filter(author__name="J.K. Rowling")

# List all books in a library.
library = Library.objects.get(name="Central Library")
books = library.books.all()

# Retrieve the librarian for a library.
library = Library.objects.get(name="Central Library")
librarian = library.librarian
