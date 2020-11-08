from django.shortcuts import render, HttpResponse
from .models import Book, Author2
from .forms import BookForm
# Create your views here.
def index(request):
    books = Book.objects.all()
    # passing data as dict to render() function
    return render(request, 'books/index.template.html', {
        'books':books
    })


def authors(request):
    authors = Author2.objects.all()
    # passing data as dict to render() function
    return render(request, 'books/authors.template.html', {
        'authors':authors
    })


def create_book(request):
    create_book_form = BookForm()
    return render(request, 'books/create_book.template.html', {
        'form':create_book_form
    })
