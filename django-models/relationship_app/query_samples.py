from relationship_app.models import Book, Library

author = "J.K. Rowling"
library_name = "Central Library"

# Query all books by a specific author.
books = Book.objects.filter(author=author)

# List all books in a library.
library = Library.objects.get(name=library_name)
books = library.books.all()

# Retrieve the librarian for a library.
library = Library.objects.get(name="Central Library")
librarian = library.librarian
