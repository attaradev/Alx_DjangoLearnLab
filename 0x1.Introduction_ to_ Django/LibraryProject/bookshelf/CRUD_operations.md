# CRUD Operations Documentation

## Create Operation

```python
from bookshelf.models import Book

# Create a Book instance with the title “1984”, author “George Orwell”, and publication year 1949.
new_book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Created: {new_book}")
```

**Expected Output:**

```sh
Created: 1984
```

## Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve and display all attributes of the book you just created.
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
```

**Expected Output:**

```sh
Title: 1984, Author: George Orwell, Publication Year: 1949
```

## Update Operation

```python
from bookshelf.models import Book

# Update the title of “1984” to “Nineteen Eighty-Four” and save the changes.
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(f"Updated Title: {book.title}")
```

**Expected Output:**

```sh
Updated Title: Nineteen Eighty-Four
```

## Delete Operation

```python
from bookshelf.models import Book

# Delete the book you created and confirm the deletion by trying to retrieve all books again.
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm deletion
books = Book.objects.all()
print(f"All Books: {list(books)}")
```

**Expected Output:**

```sh
All Books: []
```
