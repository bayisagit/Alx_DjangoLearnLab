from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('books/', ListView.as_view(), name='list-view'),  # List all books
    path('books/<int:pk>/', DetailView.as_view(), name='detail-view'),  # Retrieve a single book by ID
    path('books/create/', CreateView.as_view(), name='create-view'),  # Add a new book
    path('books/<int:pk>/books/update/', UpdateView.as_view(), name='update-view'),  # Update an existing book
    path('books/<int:pk>/books/delete', DeleteView.as_view(), name='delete-view'),  # Delete a book
]
