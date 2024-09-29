from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Book


class BookAPITests(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(
            username='testuser', password='password')
        # Create some sample books
        self.book1 = Book.objects.create(
            title='Test Book 1', author='Author 1', publication_year=2020)
        self.book2 = Book.objects.create(
            title='Test Book 2', author='Author 2', publication_year=2021)
        self.book_create_url = reverse('book-list')
        self.book_detail_url = lambda pk: reverse(
            'book-detail', kwargs={'pk': pk})

    # Test list endpoint (GET /books/) without authentication
    def test_get_books_without_auth(self):
        response = self.client.get(self.book_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Expect 2 books in the response
        self.assertEqual(len(response.data), 2)

    # Test list endpoint (GET /books/) with login
    def test_get_books_with_auth(self):
        # Log in with the created user
        self.client.login(username='testuser', password='password')

        response = self.client.get(self.book_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # Test create book endpoint (POST /books/) with authentication
    def test_create_book_with_auth(self):
        self.client.login(username='testuser',
                          password='password')  # Log in the user
        data = {'title': 'New Book', 'author': 'New Author',
                'publication_year': 2022}
        response = self.client.post(self.book_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, 'New Book')

    # Test create book without authentication
    def test_create_book_without_auth(self):
        data = {'title': 'New Book', 'author': 'New Author',
                'publication_year': 2022}
        response = self.client.post(self.book_create_url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)  # Unauthorized
