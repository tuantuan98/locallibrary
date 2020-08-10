from django.shortcuts import render
from django.views import generic
from django.shortcuts import get_object_or_404
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_books_contain_word = Book.objects.filter(title__contains='conan').count()    
    # The 'all()' is implied by default.    
    num_authors = Author.objects.count()
    num_genre = Genre.objects.count()
    
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genre': num_genre,
        'num_books_contain_word':num_books_contain_word,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2
class BookDetailView(generic.DetailView):
    model = Book
def book_detail_view(request, primary_key):
    book = get_object_or_404(Book, pk=primary_key)
    return render(request, 'catalog/book_detail.html', context={'book': book})
class AuthorsListView(generic.ListView):
    model = Author
    paginate_by = 2
class AuthorsDetailView(generic.DetailView):
    model = Author
def authors_detail_view(request, primary_key):
    author = get_object_or_404(Book, pk=primary_key)
    return render(request, 'catalog/author_detail.html', context={'author': author})
