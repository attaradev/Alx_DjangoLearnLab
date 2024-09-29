# Filtering, Searching, and Ordering in Book API

1. **Filtering**:
   - You can filter books by `title`, `author`, and `publication_year`:

     ```sh
     GET /api/books/?title=BookTitle&author=AuthorName&publication_year=2023
     ```

2. **Searching**:
   - You can search books by `title` and `author`:

     ```sh
     GET /api/books/?search=BookTitle
     ```

3. **Ordering**:
   - You can order books by `title` or `publication_year`:

     ```sh
     GET /api/books/?ordering=publication_year
     ```

4. **Combining**:
   - You can combine filtering, searching, and ordering in one query:

     ```sh
     GET /api/books/?title=BookTitle&ordering=publication_year&search=AuthorName
     ```
