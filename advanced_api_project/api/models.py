from django.db import models


class Author(models.Model):
    """
    Represents an author who writes books.

    Fields:
    - name: The name of the author.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book written by an author.

    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: A foreign key linking to the Author model.

    Relationships:
    - Each book is associated with a single author.
    - An author can have multiple books (one-to-many relationship).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
