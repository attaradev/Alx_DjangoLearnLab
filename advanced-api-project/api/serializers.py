from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializer for the Book model.

    Fields:
    - title: The title of the book.
    - publication_year: The year the book was published.
    - author: The author of the book (represented by an ID in the API).

    Validation:
    - Ensures that the publication_year is not set to a future year.
    """
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        """
        Validate that the publication_year is not in the future.

        Args:
        - value: The publication year to be validated.

        Returns:
        - The validated publication year if it is valid.

        Raises:
        - serializers.ValidationError: If the publication year is in the future.
        """
        import datetime
        if value > datetime.datetime.now().year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for the Author model.

    Fields:
    - name: The name of the author.
    - books: A nested representation of related books (using BookSerializer).

    Relationship Handling:
    - The books field is a nested serializer that includes all books related to the author.
    - The related_name='books' in the Book model's foreign key allows accessing books from an author instance.
    """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
