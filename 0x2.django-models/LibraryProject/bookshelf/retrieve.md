# Retrieve Book

```python
from bookshelf.models import Book

# Retrieve and display all attributes of the book you just created.
book = Book.objects.get(title="1984")
print(f"Title: {book.title}, Author: {book.author}, Publication Year: {book.publication_year}")
```
