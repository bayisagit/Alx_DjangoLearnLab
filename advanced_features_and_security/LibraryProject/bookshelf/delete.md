# Deleting the Book instance
from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})
# Verifying deletion
>>> books = Book.objects.all()
>>> print(f"All Books after deletion: {list(books)}")
All Books after deletion: []