create
>>> from bookshelf.models import Book
>>> Book.objects.create(
... title = "1984",
... author = "George Orwell",
... publication_year = 1949) 
<Book: Book object (1)>

Retrieve:
>>> from bookshelf.models import Book
>>> Book.objects.get(title="1984")
<Book: Book object (1)>

Update
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()

Delete
# Deleting the Book instance
from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
(1, {'bookshelf.Book': 1})
# Verifying deletion
>>> books = Book.objects.all()
>>> print(f"All Books after deletion: {list(books)}")
All Books after deletion: []