from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client = APIClient()
        
        # Authenticate the client
        self.client.login(username="testuser", password="testpassword")
        
        # Create test data
        self.author = Author.objects.create(name="Test Author")
        self.book = Book.objects.create(title="Test Book", publication_year=2023, author=self.author)

    def test_create_book(self):
        """Test creating a new book"""
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post("/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")

    def test_list_books(self):
        """Test listing all books"""
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_book(self):
        """Test retrieving a single book"""
        response = self.client.get(f"/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_update_book(self):
        """Test updating a book"""
        data = {"title": "Updated Book", "publication_year": 2024}
        response = self.client.put(f"/books/{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(f"/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books(self):
        """Test filtering books by title"""
        response = self.client.get("/books/?title=Test Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get("/books/?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books(self):
        """Test ordering books by publication_year"""
        response = self.client.get("/books/?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_permission_denied_for_unauthenticated_users(self):
        """Test that unauthenticated users cannot create, update, or delete books"""
        self.client.logout()
        
        # Attempt to create a book
        response = self.client.post("/books/", {"title": "Unauthorized Book", "publication_year": 2023, "author": self.author.id})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
        # Attempt to delete a book
        response = self.client.delete(f"/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
