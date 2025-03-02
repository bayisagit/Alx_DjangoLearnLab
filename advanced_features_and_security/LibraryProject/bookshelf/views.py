from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponseForbidden
from .forms import ExampleForm


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == "POST":
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        publication_date = request.POST.get('publication_date')
        
        book = Book.objects.create(
            title=title,
            author=author,
            description=description,
            publication_date=publication_date
        )
        return render(request, 'book_detail.html', {'book': book})
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.description = request.POST.get('description')
        book.publication_date = request.POST.get('publication_date')
        book.save()
        return render(request, 'book_detail.html', {'book': book})
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'book_list.html')

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('book_list')  
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})