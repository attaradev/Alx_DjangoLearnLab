from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book

"""
Test cases for Book API:
1. Test CRUD operations (Create, Retrieve, Update, Delete).
2. Test filtering, searching, and ordering.
3. Test permission and authentication handling.
"""


class BookAPITests(APITestCase):

    def setUp(self):
        # Create some sample books
        self.book1 = Book.objects.create(
            title='Test Book 1', author='Author 1', publication_year=2020)
        self.book2 = Book.objects.create(
            title='Test Book 2', author='Author 2', publication_year=2021)
        # Adjust the URL names to match your project
        self.book_create_url = reverse('book-list')
        self.book_detail_url = lambda pk: reverse(
            'book-detail', kwargs={'pk': pk})

    # Test list endpoint (GET /books/)
    def test_get_books(self):
        response = self.client.get(self.book_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Expect 2 books in the response
        self.assertEqual(len(response.data), 2)

    # Test retrieve endpoint (GET /books/<id>/)
    def test_get_book_by_id(self):
        response = self.client.get(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book 1')

    # Test create endpoint (POST /books/)
    def test_create_book(self):
        data = {'title': 'New Book', 'author': 'New Author',
                'publication_year': 2022}
        response = self.client.post(self.book_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    # Test update endpoint (PUT /books/<id>/)
    def test_update_book(self):
        data = {'title': 'Updated Title',
                'author': 'Updated Author', 'publication_year': 2022}
        response = self.client.put(self.book_detail_url(
            self.book1.id), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    # Test delete endpoint (DELETE /books/<id>/)
    def test_delete_book(self):
        response = self.client.delete(self.book_detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # Test filtering by title
    def test_filter_books_by_title(self):
        response = self.client.get(self.book_create_url, {
                                   'title': 'Test Book 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Test Book 1')

    # Test searching by author
    def test_search_books_by_author(self):
        response = self.client.get(self.book_create_url, {
                                   'search': 'Author 1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 1')

    # Test ordering by publication_year
    def test_order_books_by_publication_year(self):
        response = self.client.get(self.book_create_url, {
                                   'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2020)
        self.assertEqual(response.data[1]['publication_year'], 2021)

    # Test unauthorized create request
    def test_unauthorized_create_book(self):
        self.client.logout()  # Ensure no user is logged in
        data = {'title': 'Unauthorized Book',
                'author': 'No Author', 'publication_year': 2022}
        response = self.client.post(self.book_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
